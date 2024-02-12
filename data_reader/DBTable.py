"""
Define Table classes for the ORM structure
"""
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import (Column, Integer, Float, DateTime,
                        SmallInteger, String, Text, DECIMAL,
                        ForeignKey)

Base = declarative_base()

class ParkingSpace(Base):
    '''
    This class represents the parking_space table in the database.
    '''
    __tablename__ = 'parking_space'
    id = Column(Integer, primary_key=True, autoincrement=True)
    parkid = Column(SmallInteger, ForeignKey('parking_info.parkid'))
    transqty = Column(SmallInteger)
    time = Column(DateTime)
    park = relationship('ParkingInfo')


# class ParkingId(Base):
#     """
#     Table including parking id and parking name
#     """

#     __tablename__ = 'parking_id'
#     parkid = Column(SmallInteger, primary_key=True)
#     parkname = Column(String)

class ParkingInfo(Base):
    __tablename__ = 'parking_info'

    parkid = Column(SmallInteger, primary_key=True)
    parkname = Column(String)
    lon = Column("positionX", DECIMAL(precision=20, scale=15))
    lat = Column("positionY",DECIMAL(precision=20, scale=15))
    parkdesc = Column(Text)
    parkaddress = Column(Text)
    payexam = Column(Text)
    heightlimit = Column(Text)
    iconState = Column(SmallInteger)
    numM = Column(Integer)
    numS = Column(Integer)
    availableCount = Column(Integer)

class AggWeekly(Base):
    __tablename__ = 'agg_weekly'

    id    = Column(SmallInteger, primary_key=True)
    parkid = Column(SmallInteger,nullable=False)
    week_day = Column(SmallInteger, nullable=False)
    sect = Column(SmallInteger, nullable=False)
    average_space = Column("Average Space", Float, nullable=False)