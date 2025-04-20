from sqlalchemy import String,Float,Integer,Column,Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Projeto_clima2(Base):
    __tablename__ = "Clima-AnaliseTemporal"

    id = Column(Integer,primary_key=True,autoincrement=True)
    city_name = Column(String)
    cloudiness = Column(Float)
    date = Column(Date)
    description = Column(String)
    humidity = Column(Integer)
    rain = Column(Float)
    temp = Column(Integer)
    time = Column(String)
    wind_speedy = Column(Float)

