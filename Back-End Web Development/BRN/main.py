# _*_ coding: utf_8 _*_
"""
Created on Sun Feb 13 19:52:17 2022

@author: itchytummy
"""
from asyncio.windows_events import NULL
from sqlalchemy import null
import sqlalchemy.orm as orm
from fastapi import FastAPI , Depends,  Query
from typing import Optional , List
import schemas, services, models


app = FastAPI()


@app.get("/")
def root():
    return {"Bioinformatics Research Network": "Back-end Web Development Training Requirement"}


@app.get("/api/gapminder")
def get_data(db: orm.Session=Depends(services.get_db), agriculture = Depends(services.agriculture),
         year = Depends(services.year), continent= Depends(services.continent), country = Depends(services.country), 
         co2 = Depends(services.co2), domestic_credit= Depends(services.domestic_credit), 
         electric_consum = Depends(services.electric_consum), energy_use=Depends(services.energy_use),
         exports = Depends(services.exports), fertility = Depends(services.fertility), gdp_growth = Depends(services.gdp_growth),
         imports = Depends(services.imports), industry = Depends(services.industry), inflation = Depends(services.inflation),
         life_expect = Depends(services.life_expect), pop_density= Depends(services.pop_density),
         service = Depends(services.service), pop = Depends(services.pop), gdp_percap = Depends(services.gdp_percap)):
    b= services.get_data(db, agriculture, year, continent, country, 
                            co2, domestic_credit, electric_consum, energy_use,
                            exports, fertility, gdp_growth, imports,
                            industry, inflation, life_expect, pop_density, 
                            service, pop, gdp_percap)
    return b.all()


            
@app.get("/api/country")
def get_country(db: orm.Session=Depends(services.get_db), agriculture = Depends(services.agriculture),
         year = Depends(services.year), continent= Depends(services.continent), country = Depends(services.country), 
         co2 = Depends(services.co2), domestic_credit= Depends(services.domestic_credit), 
         electric_consum = Depends(services.electric_consum), energy_use=Depends(services.energy_use),
         exports = Depends(services.exports), fertility = Depends(services.fertility), gdp_growth = Depends(services.gdp_growth),
         imports = Depends(services.imports), industry = Depends(services.industry), inflation = Depends(services.inflation),
         life_expect = Depends(services.life_expect), pop_density= Depends(services.pop_density),
         service = Depends(services.service), pop = Depends(services.pop), gdp_percap = Depends(services.gdp_percap)):
    b= services.get_data(db, agriculture, year, continent, country, 
                            co2, domestic_credit, electric_consum, energy_use,
                            exports, fertility, gdp_growth, imports,
                            industry, inflation, life_expect, pop_density, 
                            service, pop, gdp_percap)
    
    country = db.query(models.gapminder).intersect(b).with_entities(models.gapminder.country).all() 
    countries = []
    for l in country: 
        if l['country'] not in countries:
            countries.append(l['country'])
    return {"countries":countries}