import folium
import csv
import pandas as pd
from textblob import TextBlob

state_geo = r'USStateMap.json'
state_unemployment = r'US_Unemployment_Oct2012.csv'

state_data = pd.read_csv(state_unemployment)
# LetFolium determine the scale

map = folium.Map(location=[48, -102], zoom_start=3)
map.geo_json(geo_path=state_geo, data=state_data,
             columns=['State', 'Unemployment'],
             key_on='feature.id',
             fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
             legend_name='Average Rate (*/5)')
map.create_map(path='us_states.html')
