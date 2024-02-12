from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st

def SQL_engine(_config)-> Engine:
    '''
    Connect and login to the database and return the engine.
    '''
    engine_string = (
        "mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        .format(**_config)
    )
    print('Connected to database.')
    return create_engine(engine_string)

def create_session(engine:Engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

@st.cache_resource
def get_session():
    _config = dict(
        host = st.secrets["db_host"],
        user =st.secrets["db_username"],
        password =st.secrets["db_password"],
        database = "Parking",
        port = 3306,
    )
    return create_session(SQL_engine(_config))