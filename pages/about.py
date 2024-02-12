import streamlit as st
from constants.style import create_topbar, import_style
from constants.text import *

st.set_page_config(
    initial_sidebar_state="collapsed",
)
import_style()
create_topbar('關於我們')

col_41, col_42 = st.columns(2, gap="large")
st.markdown("<br><br>", unsafe_allow_html=True);
with col_41:
    st.markdown(about_name1, unsafe_allow_html=True)
    st.image("images/photo_alex.jpg")
    st.markdown(about_link1, unsafe_allow_html=True)
    st.markdown(about_intro1, unsafe_allow_html=True)
with col_42:
    st.markdown(about_name2, unsafe_allow_html=True)
    st.image("images/photo_teddy.jpeg")
    st.markdown(about_link2, unsafe_allow_html=True)
    st.markdown(about_intro2, unsafe_allow_html=True)
