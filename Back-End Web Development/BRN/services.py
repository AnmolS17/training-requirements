from pyexpat import model
import sqlalchemy.orm as orm
from sqlalchemy import Column, null
from zmq import NULL
import models, schemas, database
from fastapi import Depends, Query, HTTPException
from typing import Optional


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_rows(db: orm.Session):
    return db.query(models.gapminder).all()


class year:
    def __init__(
        self,
        year: Optional[float] = Query(None, description="Year"),
        year_op: Optional[str] = "eq",
    ):
        self.value = year
        self.op = year_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.year == self.value, models.gapminder.year != ""
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.year != self.value, models.gapminder.year != ""
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.year > self.value, models.gapminder.year != ""
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.year < self.value, models.gapminder.year != ""
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class continent:
    def __init__(
        self,
        continent: Optional[str] = Query(None, description="Continent"),
        continent_op: Optional[str] = "eq",
    ):
        self.value = continent
        self.op = continent_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.continent == self.value,
                    models.gapminder.continent != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.continent != self.value,
                    models.gapminder.continent != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq' and 'neq'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class country:
    def __init__(
        self,
        country: Optional[str] = Query(None, description="Countries"),
        country_op: Optional[str] = "eq",
    ):
        self.value = country
        self.op = country_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.country == self.value,
                    models.gapminder.country != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.country != self.value,
                    models.gapminder.country != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq' and 'neq'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class co2:
    def __init__(
        self,
        co2: Optional[float] = Query(
            None, description="CO2 emissions (metric tons per capita)"
        ),
        co2_op: Optional[str] = "eq",
    ):
        self.value = co2
        self.op = co2_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.co2_emissions == self.value,
                    models.gapminder.co2_emissions != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.co2_emissions != self.value,
                    models.gapminder.co2_emissions != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.co2_emissions > self.value,
                    models.gapminder.co2_emissions != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.co2_emissions < self.value,
                    models.gapminder.co2_emissions != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class domestic_credit:
    def __init__(
        self,
        domestic_credit: Optional[float] = Query(
            None, description="Domestic credit provided by financial sector (% of GDP)"
        ),
        domestic_credit_op: Optional[str] = "eq",
    ):
        self.value = domestic_credit
        self.op = domestic_credit_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.domestic_credit == self.value,
                    models.gapminder.domestic_credit != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.domestic_credit != self.value,
                    models.gapminder.domestic_credit != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.domestic_credit > self.value,
                    models.gapminder.domestic_credit != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.domestic_credit < self.value,
                    models.gapminder.domestic_credit != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class electric_consum:
    def __init__(
        self,
        electric_consum: Optional[float] = Query(
            None, description="Electric power consumption (kWh per capita)"
        ),
        electric_consum_op: Optional[str] = "eq",
    ):
        self.value = electric_consum
        self.op = electric_consum_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.electric_power == self.value,
                    models.gapminder.electric_power != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.electric_power != self.value,
                    models.gapminder.electric_power != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.electric_power > self.value,
                    models.gapminder.electric_power != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.electric_power < self.value,
                    models.gapminder.electric_power != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class energy_use:
    def __init__(
        self,
        energy_use: Optional[float] = Query(
            None, description="Energy use (kg of oil equivalent per capita)"
        ),
        energy_use_op: Optional[str] = "eq",
    ):
        self.value = energy_use
        self.op = energy_use_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.energy_use == self.value,
                    models.gapminder.energy_use != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.energy_use != self.value,
                    models.gapminder.energy_use != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.energy_use > self.value,
                    models.gapminder.energy_use != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.energy_use < self.value,
                    models.gapminder.energy_use != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class exports:
    def __init__(
        self,
        exports: Optional[float] = Query(
            None, description="Exports of goods and services (% of GDP)"
        ),
        exports_op: Optional[str] = "eq",
    ):
        self.value = exports
        self.op = exports_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.exports == self.value,
                    models.gapminder.exports != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.exports != self.value,
                    models.gapminder.exports != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.exports > self.value,
                    models.gapminder.exports != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.exports < self.value,
                    models.gapminder.exports != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class fertility:
    def __init__(
        self,
        fertility: Optional[float] = Query(
            None, description="Fertility rate, total (births per woman)"
        ),
        fertility_op: Optional[str] = "eq",
    ):
        self.value = fertility
        self.op = fertility_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.fertility_rate == self.value,
                    models.gapminder.fertility_rate != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.fertility_rate != self.value,
                    models.gapminder.fertility_rate != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.fertility_rate > self.value,
                    models.gapminder.fertility_rate != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.fertility_rate < self.value,
                    models.gapminder.fertility_rate != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class gdp_growth:
    def __init__(
        self,
        gdp_growth: Optional[float] = Query(None, description="GDP growth (annual %)"),
        gdp_growth_op: Optional[str] = "eq",
    ):
        self.value = gdp_growth
        self.op = gdp_growth_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.gdp_growth == self.value,
                    models.gapminder.gdp_growth != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.gdp_growth != self.value,
                    models.gapminder.gdp_growth != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.gdp_growth > self.value,
                    models.gapminder.gdp_growth != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.gdp_growth < self.value,
                    models.gapminder.gdp_growth != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class imports:
    def __init__(
        self,
        imports: Optional[float] = Query(
            None, description="Imports of goods and services (% of GDP)"
        ),
        imports_op: Optional[str] = "eq",
    ):
        self.value = imports
        self.op = imports_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.imports == self.value,
                    models.gapminder.imports != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.imports != self.value,
                    models.gapminder.imports != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.imports > self.value,
                    models.gapminder.imports != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.imports < self.value,
                    models.gapminder.imports != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class industry:
    def __init__(
        self,
        industry: Optional[float] = Query(
            None, description="Industry, value added (% of GDP)"
        ),
        industry_op: Optional[str] = "eq",
    ):
        self.value = industry
        self.op = industry_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.industry == self.value,
                    models.gapminder.industry != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.industry != self.value,
                    models.gapminder.industry != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.industry > self.value,
                    models.gapminder.industry != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.industry < self.value,
                    models.gapminder.industry != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class inflation:
    def __init__(
        self,
        inflation: Optional[float] = Query(
            None, description="Inflation, GDP deflator (annual %)"
        ),
        inflation_op: Optional[str] = "eq",
    ):
        self.value = inflation
        self.op = inflation_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.inflation == self.value,
                    models.gapminder.inflation != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.inflation != self.value,
                    models.gapminder.inflation != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.inflation > self.value,
                    models.gapminder.inflation != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.inflation < self.value,
                    models.gapminder.inflation != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class life_expect:
    def __init__(
        self,
        life_expect: Optional[float] = Query(
            None, description="Life expectancy at birth, total (years)"
        ),
        life_expect_op: Optional[str] = "eq",
    ):
        self.value = life_expect
        self.op = life_expect_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.life_expectancy == self.value,
                    models.gapminder.life_expectancy != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.life_expectancy != self.value,
                    models.gapminder.life_expectancy != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.life_expectancy > self.value,
                    models.gapminder.life_expectancy != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.life_expectancy < self.value,
                    models.gapminder.life_expectancy != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class pop_density:
    def __init__(
        self,
        pop_density: Optional[float] = Query(
            None, description="Population density (people per sq. km of land area)"
        ),
        pop_density_op: Optional[str] = "eq",
    ):
        self.value = pop_density
        self.op = pop_density_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.pop_density == self.value,
                    models.gapminder.pop_density != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.pop_density != self.value,
                    models.gapminder.pop_density != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.pop_density > self.value,
                    models.gapminder.pop_density != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.pop_density < self.value,
                    models.gapminder.pop_density != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class service:
    def __init__(
        self,
        services: Optional[float] = Query(
            None, description="Services, etc., value added (% of GDP)"
        ),
        services_op: Optional[str] = "eq",
    ):
        self.value = services
        self.op = services_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.services == self.value,
                    models.gapminder.services != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.services != self.value,
                    models.gapminder.services != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.services > self.value,
                    models.gapminder.services != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.services < self.value,
                    models.gapminder.services != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class pop:
    def __init__(
        self,
        pop: Optional[float] = Query(None, description="Population"),
        pop_op: Optional[str] = "eq",
    ):
        self.value = pop
        self.op = pop_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.pop == self.value, models.gapminder.pop != ""
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.pop != self.value, models.gapminder.pop != ""
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.pop > self.value, models.gapminder.pop != ""
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.pop < self.value, models.gapminder.pop != ""
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)
        return query


class gdp_percap:
    def __init__(
        self,
        gdp_percap: Optional[float] = Query(None, description="GDP per capita"),
        gdp_percap_op: Optional[str] = "eq",
    ):
        self.value = gdp_percap
        self.op = gdp_percap_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.gdp_percap == self.value,
                    models.gapminder.gdp_percap != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.gdp_percap != self.value,
                    models.gapminder.gdp_percap != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.gdp_percap > self.value,
                    models.gapminder.gdp_percap != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.gdp_percap < self.value,
                    models.gapminder.gdp_percap != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)

        return query


class agriculture:
    def __init__(
        self,
        agriculture: Optional[float] = Query(
            None, description="Agriculture, value added (% of GDP)"
        ),
        agriculture_op: Optional[str] = "eq",
    ):
        self.value = agriculture
        self.op = agriculture_op

    def query(db: orm.Session, self):
        if self.value:
            if self.op == "eq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.agriculture == self.value,
                    models.gapminder.agriculture != "",
                )
            elif self.op == "neq":
                query = db.query(models.gapminder).filter(
                    models.gapminder.agriculture != self.value,
                    models.gapminder.agriculture != "",
                )
            elif self.op == "gt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.agriculture > self.value,
                    models.gapminder.agriculture != "",
                )
            elif self.op == "lt":
                query = db.query(models.gapminder).filter(
                    models.gapminder.agriculture < self.value,
                    models.gapminder.agriculture != "",
                )
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operator: choose between 'eq','neq','gt' and 'lt'.",
                )
        else:
            query = db.query(models.gapminder)

        return query


def get_data(
    db: orm.Session,
    agriculture_=Depends(agriculture),
    year_=Depends(year),
    continent_=Depends(continent),
    country_=Depends(country),
    co2_=Depends(co2),
    domestic_credit_=Depends(domestic_credit),
    electric_consum_=Depends(electric_consum),
    energy_use_=Depends(energy_use),
    exports_=Depends(exports),
    fertility_=Depends(fertility),
    gdp_growth_=Depends(gdp_growth),
    imports_=Depends(imports),
    industry_=Depends(industry),
    inflation_=Depends(inflation),
    life_expect_=Depends(life_expect),
    pop_density_=Depends(pop_density),
    services_=Depends(service),
    pop_=Depends(pop),
    gdp_percap_=Depends(gdp_percap),
):
    agri_q = agriculture.query(db, agriculture_)
    year_q = year.query(db, year_)
    continent_q = continent.query(db, continent_)
    country_q = country.query(db, country_)
    co2_q = co2.query(db, co2_)
    dom_cred_q = domestic_credit.query(db, domestic_credit_)
    elec_q = electric_consum.query(db, electric_consum_)
    energy_q = energy_use.query(db, energy_use_)
    exp_q = exports.query(db, exports_)
    fert_q = fertility.query(db, fertility_)
    gdp_growth_q = gdp_growth.query(db, gdp_growth_)
    imp_q = imports.query(db, imports_)
    ind_q = industry.query(db, industry_)
    infl_q = inflation.query(db, inflation_)
    life_q = life_expect.query(db, life_expect_)
    pop_den_q = pop_density.query(db, pop_density_)
    services_q = service.query(db, services_)
    pop_q = pop.query(db, pop_)
    gdp_percap_q = gdp_percap.query(db, gdp_percap_)

    query = db.query(models.gapminder).intersect(
        agri_q,
        year_q,
        continent_q,
        country_q,
        co2_q,
        dom_cred_q,
        elec_q,
        energy_q,
        exp_q,
        fert_q,
        gdp_growth_q,
        imp_q,
        ind_q,
        infl_q,
        life_q,
        pop_den_q,
        services_q,
        pop_q,
        gdp_percap_q,
    )

    return query
