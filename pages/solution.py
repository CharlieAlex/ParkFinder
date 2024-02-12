import streamlit as st
import pipeline.features as FE
from data_reader import get_session
from datetime import time, timedelta
from constants.option import parking_options, district_options
import warnings
import plotly.express as px
from constants.style import create_topbar, import_style
warnings.filterwarnings("ignore", category=FutureWarning, module="_plotly_utils.basevalidators")
px.set_mapbox_access_token(st.secrets["map_token"])

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
)
import_style()
create_topbar('解決方案')

session = get_session()
input_options = dict()
parking_lot_based_keys = list(FE.feature_options.keys())[:2]
map_based_keys = list(FE.feature_options)[2:]

feature_name = st.selectbox(
    label="請選擇功能",
    options=FE.feature_options.keys(),
)

with st.form(key="submit"):
    if feature_name in parking_lot_based_keys:
        selection_content= st.multiselect(
            label="請選擇停車場",
            placeholder = "",
            options=parking_options.keys()
        )
        input_options['ids'] = {parking_options[pn] for pn in selection_content}
        if feature_name == parking_lot_based_keys[0]:    ## 歷史
            dow = st.select_slider("星期", FE.DAYOFWEEK_STR_MAP.values(), key="週日")

    if feature_name in map_based_keys:
        init_location = st.selectbox(
            label="請選擇行政區域",
            options=district_options.keys()
        )
        dow = st.select_slider("星期", FE.DAYOFWEEK_STR_MAP.values())
        time_to_plot = st.slider("時間",min_value=time(0,0), max_value=time(23,0), value=time(9,0), step=timedelta(hours=1))
        input_options['t'] = time_to_plot

    submit_button = st.form_submit_button(label="開始搜尋")

if submit_button:
    with st.spinner("請耐心等候資料擷取，約需30秒..."):
        try:
            fe = FE.feature_factory(feature_name, **input_options)
            load_data = fe.load_data_from_db(session)

            if feature_name == list(FE.feature_options.keys())[0]:
                fe.set_plot_weekday(FE.DAYOFWEEK_SRT_ENUM_MAP[dow])
            if feature_name in map_based_keys:
                fe.set_plot_time(FE.DAYOFWEEK_SRT_ENUM_MAP[dow], time_to_plot)
                fe.set_plot_init(district_options[init_location])
            fig = fe.plotly_figure()
            st.plotly_chart(fig, use_container_width=True)

        except:
            st.write("資料擷取錯誤，請嘗試重新搜尋！")