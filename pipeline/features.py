"""
Each Feature class represents a set of SQL command, column generation ,rule of aggregation, and visualization
"""

from abc import ABC, abstractmethod
from functools import lru_cache, cached_property
import pandas as pd
from plotly.graph_objects import Figure
import plotly.express as px
from sqlalchemy.orm import Query, Session
from sqlalchemy import func
import datetime

from data_reader.DBTable import ParkingInfo, ParkingSpace, AggWeekly
from pipeline.helper import line_with_errors
from data_reader.api import TimeSection

from typing import List, Dict, Union, Tuple, Callable
from enum import IntEnum

import streamlit as st

HOUR = 1e9*3600
DAYOFWEEK_STR_MAP = {i+1 :f"週{v}" for i,v in enumerate("日一二三四五六")}

DAAN_INIT_COORD = (25.02489196326003, 121.54339897225)

class DAYOFWEEK(IntEnum):
    SUNDAY      = 1
    MONDAY      = 2
    TUESDAY     = 3
    WEDNESDAY   = 4
    THURSDAY    = 5
    FRIDAY      = 6
    SATURDAY    = 7

DAYOFWEEK_SRT_ENUM_MAP = {k: DAYOFWEEK(i) for i,k in DAYOFWEEK_STR_MAP.items()}

class BaseFeatureClass(ABC):

    @abstractmethod
    def load_data_from_db(self, session: Session):
        ...

    def load_data_from_api(self, **kwargs):
        ...

    @property
    @abstractmethod
    def dataframe(self):
        ...

    @abstractmethod
    def plotly_figure(self) -> Figure:
        ...

class FakeFE(BaseFeatureClass):
    def __init__(self, num:int, **kargs) -> None:
        self.num = num
    def load_data_from_db(self, session: Session):
        return {'Name': 'Pakr'}

    def dataframe(self):
        return pd.DataFrame()

    def set_plot_weekday(self, dow:DAYOFWEEK):
        self.num *= dow.value

    def plotly_figure(self) -> Figure:
        import numpy as np

        fig = px.scatter(x= np.random.rand(self.num), y= np.random.rand(self.num))
        return fig

class WeekdayAverageByHour(BaseFeatureClass):
    def __init__(self, ids:List[int],
                 time_interval:int = 20,
                 ) -> None:
        self.parking_ids = tuple(ids)
        self.time_interval = time_interval
        self.dow_to_plot = DAYOFWEEK.MONDAY

    @lru_cache
    def load_data_from_db(self, session: Session):
        """
        Executes query and retrieves data from database.
        Might want to explore designs that allow different types of data-loading process,
        such as if user wants to load from api.
        """
        results = self.query_object.with_session(session)
        try:
            self.results = results.all()
        except Exception as e:
            print(f"Error during database query: {e}")
            self.results = []
            session.rollback()
        return self.results

    @property
    def query_object(self) -> Query:
        """
        The auto-generated `sqlalchemy.orm.Query` object from ids passed in the class constructor.
        """
        subquery = (
            Query([
                ParkingInfo.parkname                  .label('Name'),
                ParkingSpace.time,
                ParkingSpace.transqty               .label('space'),
                ((
                    func.hour(ParkingSpace.time) * 60 +
                    func.minute(ParkingSpace.time)
                ) // self.time_interval
                )                                   .label('sect'),
                func.dayofweek(ParkingSpace.time)   .label('week_day')
            ])
            .join(ParkingSpace, ParkingSpace.parkid == ParkingInfo.parkid)
            .filter(
                ParkingSpace.parkid.in_(self.parking_ids)
                )
            .subquery()
        )

        # Build the main query
        main_query = (
            Query([
                subquery.c.Name,
                subquery.c.week_day     .label("week_day"),
                subquery.c.sect         .label("time_section"),
                func.AVG(subquery.c.space).label('average_space'),
                func.STDDEV(subquery.c.space).label('std')
            ])
            .group_by(subquery.c.Name, subquery.c.week_day, subquery.c.sect)
            .order_by(subquery.c.Name.desc(), subquery.c.week_day, subquery.c.sect)
        )

        return main_query

    @cached_property
    def dataframe(self):
        try:
            df = pd.DataFrame(self.results)
            ts = TimeSection(self.time_interval)
            df['time'] = pd.to_timedelta(ts(df['time_section']).astype(str))
            df['average_space'] = df['average_space'].astype(int)
            self.df = df
        except:
            self.df = pd.DataFrame()
        return self.df

    def set_plot_weekday(self, dow:DAYOFWEEK):
        self.dow_to_plot = dow
        return

    def plotly_figure(self) -> Figure:
        dow = self.dow_to_plot
        plotly_plot_df = self.dataframe.query("week_day == @dow").assign(time = self.dataframe['time'] + pd.Timestamp("1970/01/01") )

        fig = line_with_errors(
            error_y_mode = "band",
            data_frame = plotly_plot_df,
            x = "time",
            y = "average_space",
            error_y = "std",
            color = "Name",
            labels = {
                'time': '時段',
                'average_space': '數量',
                'Name': '名稱',
            },
        )

        fig.update_layout(
            xaxis_tickformat='%H:%M',
            title = f"{DAYOFWEEK_STR_MAP[dow]}各時段平均剩餘車位",
            legend=dict(orientation="h", y=-0.1, x=-0.1),
            hovermode="x"
            )

        return fig


class TimelineByIds(BaseFeatureClass):
    def __init__(self, ids:List[int], **kargs) -> None:
        self.parking_ids = ids

    @lru_cache
    def load_data_from_db(self, session:Session):
        """
        Executes query and retrieves data from database.
        Might want to explore designs that allow different types of data-loading process,
        such as if user wants to load from api.
        """
        results = self.query_object.with_session(session)
        try:
            self.results = results.all()
        except Exception as e:
            print(f"Error during database query: {e}")
            self.results = []
            session.rollback()
        return self.results

    @property
    def query_object(self) -> Query:
        """
        The auto-generated `sqlalchemy.orm.Query` object from ids passed in the class constructor.
        """
        main_query = (
            Query([
                ParkingInfo.parkname                  .label('Name'),
                ParkingSpace.time,
                ParkingSpace.transqty               .label('space'),
            ])
            .join(ParkingSpace, ParkingSpace.parkid == ParkingInfo.parkid)
            .filter(
                ParkingSpace.parkid.in_(self.parking_ids)
                )
        )
        return main_query

    @property
    def dataframe(self):
        self.df = pd.DataFrame(self.results)
        return self.df

    def plotly_figure(self) -> Figure:
        fig = px.line(self.dataframe, x='time', y='space', color= "Name",
                       title='歷史空位',
                       labels={
                           'Name': '停車場',
                           'time': '時間',
                           'space': '空位',
                       })

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeslider_thickness=0.1,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="一天", step="day", stepmode="backward"),
                    dict(count=7, label="一週", step="day", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )

        fig.update_layout(
            legend=dict(orientation="h", y=-2.1, x=-0.1),
            hovermode="x unified"
        )

        return fig

class WeekdayAverageMap(WeekdayAverageByHour):

    def __init__(self,
                 day_of_week: DAYOFWEEK = DAYOFWEEK.MONDAY,
                 t: datetime.time = datetime.time(9,0),
                 time_interval:int = 60) -> None:
        self.set_plot_time(day_of_week, t)
        self.time_interval = time_interval

    @lru_cache
    def load_data_from_db(self, session:Session):
        """
        Executes query and retrieves data from database.
        Might want to explore designs that allow different types of data-loading process,
        such as if user wants to load from api.
        """
        results = self.query_object.with_session(session)
        try:
            self.results = results.all()
        except Exception as e:
            print(f"Error during database query: {e}")
            self.results = []
            session.rollback()
        return self.results

    @property
    def query_object(self) -> Query:
        """
        The auto-generated `sqlalchemy.orm.Query` object from ids passed in the class constructor.
        Basically draws all ids
        """

        query = Query(
            [ParkingInfo.parkname.label("Name"),
            ParkingInfo.lat, ParkingInfo.lon,
            AggWeekly.average_space, AggWeekly.sect, AggWeekly.week_day]).join(ParkingInfo, AggWeekly.parkid == ParkingInfo.parkid)

        return query

    @cached_property
    def dataframe(self):
        self.df = pd.DataFrame(self.results)
        self.df[['lat', 'lon']] = self.df[['lat', 'lon']].astype(float)
        self.df[['average_space']] = self.df[['average_space']].astype(int)
        return self.df

    def set_plot_time(self, weekday: DAYOFWEEK, time_section:Union[str, datetime.time]):
        self.weekday_to_plot = weekday
        if isinstance(time_section, str):
            self.time_to_plot = datetime.time.fromisoformat(time_section)
        elif isinstance(time_section, datetime.time):
            self.time_to_plot = time_section
        else:
            raise ValueError("Error time parameter")

    def set_plot_init(self, init_location: Tuple[float, float]):
        self.init_location = init_location
        return

    def plotly_figure(self) -> Figure:
        dow = self.weekday_to_plot,
        sect = TimeSection(self.time_interval).time2seg(self.time_to_plot)
        plot_df = self.dataframe.query(
            "(sect == @sect) & (week_day == @dow)"
        ).copy()
        plot_df['scale'] = (
            (plot_df["average_space"] - plot_df["average_space"].min())
            /
            ((plot_df["average_space"].max() - plot_df["average_space"].min()) / 20)
        ) + 1
        fig = px.scatter_mapbox(
            plot_df,
            lat='lat', lon='lon',
            size = 'scale',
            # mapbox_style='open-street-map',
            hover_name= "Name",
            hover_data={
                "lat":False, "lon":False,
                "scale":False, "Name":False, "average_space":True,
            },
            labels = {
                "Name":"名稱",
                "average_space": "平均剩餘"
            },
            center=self.init_location,
            zoom=13,
        )

        fig.update_layout(
            mapbox_style="mapbox://styles/ted21019/clmtgbew6020901rdcfyi2nrf"
        )

        return fig

def feature_ready(fe:BaseFeatureClass):
    try:
        if len(fe.dataframe) == 0:
            return False
        return True
    except:
        return False

feature_options= ({
    "停車場平均可停車位": WeekdayAverageByHour,
    "停車場歷史可停車位": TimelineByIds,
    "停車場地圖": WeekdayAverageMap,
})

@st.cache_resource(show_spinner=True, validate=feature_ready)
def feature_factory(feature_name:str, **kwargs) -> BaseFeatureClass:
    if feature_name not in feature_options:
        raise KeyError("Feature name not found!")
    fe = feature_options[feature_name](**kwargs)
    return fe