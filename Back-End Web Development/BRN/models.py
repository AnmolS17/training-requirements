from sqlalchemy import Column, Integer, String, Float
from database import Base


class gapminder(Base):
    __tablename__ = "gapminder_tbl"
    index = Column(Integer, primary_key=True)
    country = Column(String)
    year = Column(Integer)
    agriculture = Column(Float)
    co2_emissions = Column(Integer)
    domestic_credit = Column(Integer)
    electric_power = Column(Integer)
    energy_use = Column(Integer)
    exports = Column(Integer)
    fertility_rate = Column(Integer)
    gdp_growth = Column(Integer)
    imports = Column(Integer)
    industry = Column(Integer)
    inflation = Column(Integer)
    life_expectancy = Column(Integer)
    pop_density = Column(Integer)
    services = Column(Integer)
    pop = Column(Integer)
    continent = Column(String)
    gdp_percap = Column(Integer)
