import streamlit as st
from constants.style import create_topbar, import_style
from constants.text import *

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
)
import_style()
create_topbar('技術細節')

st.divider()
st.markdown(tech_title1, unsafe_allow_html=True)
st.divider()

col_31, col_32, col_33 = st.columns(3, gap="large")
with col_31:
    st.image("images/aws.png")
    st.markdown(tech_logo1, unsafe_allow_html=True)
with col_32:
    st.image("images/taipei_gov.png")
    st.markdown(tech_logo2, unsafe_allow_html=True)
with col_33:
    st.image("images/sql.png")
    st.markdown(tech_logo3, unsafe_allow_html=True)

st.divider()
st.markdown(tech_title2, unsafe_allow_html=True)
st.divider()

col_41, col_42, col_43 = st.columns(3, gap="large")
with col_41:
    st.image("images/pandas.png")
    st.markdown(tech_logo4, unsafe_allow_html=True)
with col_42:
    st.image("images/visual_tool.png")
    st.markdown(tech_logo5, unsafe_allow_html=True)
with col_43:
    st.image("images/streamlit.png")
    st.markdown(tech_logo6, unsafe_allow_html=True)

st.divider()