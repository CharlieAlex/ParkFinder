from typing import Union
import datetime
import numpy as np
import pandas as pd

class TimeSection:
    """
    Helper function that transforms time segments into `datetime.time` objects

    ---
    Input:
        interval: minutes, indicating the interval of segmentation (minutes)
    """
    def __init__(self, interval:int = 20) -> None:
        self.interval = interval

    def _get_by_time_section(self, section_no:int) -> datetime.time:
        """
        Transfers one segment number into datetime.time object
        """
        minutes_pass = self.interval * section_no
        return datetime.time(hour=minutes_pass // 60 , minute= minutes_pass % 60)

    def vectorized_get_by_time_section(self, section_nos: Union[np.ndarray, pd.Series]) -> np.ndarray:
        """
        Vectorizes the `_get_by_time_section` function to better adapt with numpy or pandas functions,
        This allows users to transfer the data by patch.
        """
        return np.vectorize(self._get_by_time_section)(section_nos)

    def __call__(self, section_nos:Union[np.ndarray, pd.Series]):
        """
        Transforms a number or batch of numbers (np array or Series) into `datetime.time` object
        """
        return self.vectorized_get_by_time_section(section_nos)

    def time2seg(self, t:datetime.time):
        return ( 60 * t.hour + t.minute ) // self.interval