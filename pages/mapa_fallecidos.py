#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:40:49 2023

@author: pablo
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos desde el archivo CSV
datos = pd.read_csv("https://raw.githubusercontent.com/perico3372/proyecto_individual_2/main/pages/mapa.csv")

#print()

# Crear la visualización del mapa con Plotly Express
map_fatalities = px.choropleth(datos, locations='location_country', locationmode='country names', color='fatalities',
                    color_continuous_scale='Viridis',
                    title='Cantidad de accidentes por país')

# Configurar la aplicación Streamlit y mostrar la visualización del mapa
st.title("Mapa de fallecidos por país")
st.plotly_chart(map_fatalities)

# Crear la visualización del mapa con Plotly Express
map_accidents = px.choropleth(datos, locations='location_country', locationmode='country names', color='accidents',
                    color_continuous_scale='Viridis',
                    title='Cantidad de accidentes por país')

# Configurar la aplicación Streamlit y mostrar la visualización del mapa
st.title("Mapa de Accidentes por país")
st.plotly_chart(map_accidents)


