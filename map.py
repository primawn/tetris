import streamlit as st
import pandas as pd
import numpy as np
import json
from geopy.geocoders import Nominatim 
import folium # map rendering library
import data
from streamlit_folium import folium_static 

data_all = data.datajawa
data_geo = json.load(open('./indonesia-province.json'))

def center():
   address = 'Pekalongan, ID'
   geolocator = Nominatim(user_agent="id_explorer")
   location = geolocator.geocode(address)
   latitude = location.latitude
   longitude = location.longitude
   return latitude, longitude
   
data_all['Provinsi'] = [x.upper() for x in data_all['Provinsi']]

dicts = {"Penderita Tuberkulosis":'Penderita Tuberkulosis',
         "Penderita Diabetes": 'Penderita Diabetes'}

#for changing type of the maps
add_select = st.sidebar.selectbox("Jenis Peta yang Ingin Anda Tampilkan?",("OpenStreetMap", "Stamen Terrain","Stamen Toner"))

select_data = st.sidebar.radio("Data apa yang ingin Anda lihat?", ("Penderita Tuberkulosis", "Penderita Diabetes"))
data_all = pd.DataFrame(data_all)

#for calling the function for getting center of maps
centers = center()
#showing the maps
map_sby = folium.Map(tiles=add_select, location=[centers[0], centers[1]], zoom_start=6.5)

def threshold(data):
   threshold_scale = np.linspace(data_all[dicts[data]].min(), data_all[dicts[data]].max(), 10, dtype=float)
   # change the numpy array to a list
   threshold_scale = threshold_scale.tolist() 
   threshold_scale[-1] = threshold_scale[-1]
   return threshold_scale
def show_maps(data, threshold_scale):
   maps = folium.Choropleth(geo_data = data_geo,
                           data = data_all,
                           columns=['Provinsi',dicts[data]],
                           key_on='feature.properties.Propinsi',
                           threshold_scale=threshold_scale,
                           fill_color='YlOrRd',
                           fill_opacity=0.7,
                           line_opacity=0.2,
                           legend_name=dicts[data],
                           highlight=True,
                           reset=True).add_to(map_sby)
   folium_static(map_sby)
