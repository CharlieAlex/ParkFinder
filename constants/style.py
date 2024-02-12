import base64
import streamlit as st

LOGO_IMG = base64.b64encode(open("images/logo.png", "rb").read()).decode()

def import_style():
    with open("constants/style.css", "r") as file:
        css_content = file.read()
    st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
    return None

def create_topbar(page:str):
    active_dict = {
        '首頁': '',
        '解決方案': '',
        '技術細節': '',
        '關於我們': '',
    }
    active_dict[page] = 'active'

    #https://discuss.streamlit.io/t/nav-bar-disappears-using-fixed-top-argument/28224/3
    st.markdown(
        f"""
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <nav class="navbar fixed-top navbar-expand navbar-dark  d-flex flex-column flex-sm-row" style="background-color: #3498DB;">
            <a class="navbar-brand" href="./" target="_self">
                <div>
                    <img class = "logo-img" src="data:image/png;base64,{LOGO_IMG}">
                    <span> ParkFinder </span>
                </div>
            </a>
            <div class="collapse d-flex flex-column justify-content-between" id="navbarNav">
                <ul class="navbar-nav ">
                    <li class="nav-item">
                        <a class="nav-link {active_dict['首頁']}" href="./", target="_self"><b>首頁介紹</b></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {active_dict['解決方案']}" href="/solution" target="_self"><b>主要功能</b></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {active_dict['技術細節']}" href="/tech" target="_self"><b>技術細節</b></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {active_dict['關於我們']}" href="/about" target="_self"><b>關於我們</b></a>
                    </li>
                </ul>
            </div>
        </nav>
        """, unsafe_allow_html=True
    )
    return None
