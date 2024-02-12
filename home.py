# streamlit run home.py
import streamlit as st
from constants.text import *
from constants.style import create_topbar, import_style
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
)
import_style()
create_topbar('首頁')

st.markdown("<h1 color: white;></h1>",unsafe_allow_html=True)
st.markdown("<h1 color: white;></h1>",unsafe_allow_html=True)
st.markdown("<h1 color: white;></h1>",unsafe_allow_html=True)
st.markdown("<h1 color: white;></h1>",unsafe_allow_html=True)
st.markdown(home_slogan, unsafe_allow_html=True)
st.markdown("<h1 color: white;></h1>",unsafe_allow_html=True)

butcol_01, butcol_02, butcol_03 = st.columns(3, gap="large")
with butcol_02:
    if st.button('立即使用'):
        switch_page("solution")
st.markdown("<h1 color: white;></h1>",unsafe_allow_html=True)
st.markdown("<h1 color: white;></h1>",unsafe_allow_html=True)

st.divider()
st.markdown(home_title1, unsafe_allow_html=True)
st.divider()

col_01, col_02 = st.columns(2, gap="large")
with col_01:
    st.markdown(home_case1_title, unsafe_allow_html=True)
    st.image("images/park_lot_crop.jpg")
    st.markdown(home_case1_text, unsafe_allow_html=True)
    with st.expander(label="現有工具有何不足？"):
        st.markdown(home_case1_expander, unsafe_allow_html=True)
with col_02:
    st.markdown(home_case2_title, unsafe_allow_html=True)
    st.image("images/park_lottery.png")
    st.markdown(home_case2_text, unsafe_allow_html=True)
    with st.expander(label="為什麼不直接找離我最近的停車場就好？"):
        st.markdown(home_case2_expander, unsafe_allow_html=True)

st.divider()
st.markdown(home_title2, unsafe_allow_html=True)
st.divider()

col_11, col_12 = st.columns(2, gap="large")
with col_11:
    st.markdown(home_func1_title, unsafe_allow_html=True)
    st.image("images/feature_1.png")
    st.markdown(home_func1_text, unsafe_allow_html=True)
with col_12:
    st.markdown(home_func2_title, unsafe_allow_html=True)
    st.image("images/feature_2.png")
    st.markdown(home_func2_text, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True);

col_21, col_22 = st.columns(2, gap="large")
with col_21:
    st.markdown(home_func3_title, unsafe_allow_html=True)
    st.image("images/feature_3.png")
    st.markdown(home_func3_text, unsafe_allow_html=True)
with col_22:
    st.markdown(home_func4_title, unsafe_allow_html=True)
    st.image("images/feature_4.png")
    st.markdown(home_func4_text, unsafe_allow_html=True)

st.divider()