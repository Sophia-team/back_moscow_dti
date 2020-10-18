from typing import Optional
from fastapi import FastAPI
import geopandas as gpd
import pandas as pd



app = FastAPI()

geo_data = gpd.gpd.read_file('geo.json')
stats_data = pd.read_csv('graph_stats.csv')
data = pd.read_csv('lon_lat_names.csv')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/stats/scenario/{day}/{start}/{end}")
def read_item(scenario: int, day: int, start: float, end: float):
    if scenario == 0:
        col_name = 'rel'
    else:
        col_name = 'rel_{}'.format(scenario)

    answer = geo_data[(geo_data.date == day) & (geo_data[col_name] >= start) & (geo_data[col_name] < end)]
    return answer.to_json()



