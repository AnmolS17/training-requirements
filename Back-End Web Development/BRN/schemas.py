from typing import Optional
# from click import style

from pydantic import BaseModel, validator
from fastapi import Query , Depends

class gapminder(BaseModel):
    index : Optional[int] = None
    country : Optional[str] = None
    year : Optional[int] = None
    continent : Optional[str] = None
    agriculture : Optional[float] = None
    co2_emissions : Optional[float] = None
    domestic_credit : Optional[float] = None
    electric_power : Optional[float] = None
    energy_use : Optional[float] = None
    exports : Optional[float] = None
    fertility_rate : Optional[float] = None
    gdp_growth : Optional[float] = None
    imports : Optional[float] = None
    industry : Optional[float] = None
    inflation : Optional[float] = None
    life_expectancy : Optional[float] = None
    pop_density : Optional[float] = None
    services : Optional[float] = None
    pop : Optional[float] = None
    gdp_percap : Optional[float] = None

    @validator('*', pre=True)
    def blank_strings(cls, v):
        print(v)
        if v == "":
            return None
        return v
    
    class Config:
        orm_mode = True
