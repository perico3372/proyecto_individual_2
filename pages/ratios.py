#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 11:40:14 2023

@author: pablo
"""

import numpy as np

from pyspark.sql import SparkSession
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

col1, col2 = st.columns(2)

data = pd.read_csv("https://raw.githubusercontent.com/perico3372/proyecto_individual_2/main/pages/dataframe_final.csv")

####################################
##Fallecidos/Cantidad de pasajeros##
####################################

limite_inferior_ratio_fatalities = st.slider("Definir limite inferior(Año)", 1969, 1980, 2021)
data_ratio_passengers = data[data['year'] > limite_inferior_ratio_fatalities]
diff_value_ratio_passengers = np.diff(data_ratio_passengers["ratio_passengers"], prepend=0)

# Crear el gráfico de cascada con plotly

fig_ratio_passengers = go.Figure(go.Waterfall(
    name="",
    orientation="v",
    x=data_ratio_passengers['year'].astype(str),
    y=diff_value_ratio_passengers,
    textposition="inside",
    #text=df['Valor'],
    connector={"line": {"color": "rgb(63, 63, 63)"}},
))

# Crear el gráfico de líneas

x_line = data_ratio_passengers['year']
y_line = data_ratio_passengers["ratio_passengers"]
fig_ratio_passengers.add_trace(go.Scatter(
    x=x_line,
    y=y_line,
    mode='lines',
    name='Línea',
    ))
    
    # Personalizar el gráfico
fig_ratio_passengers.update_layout(
    title="Ratio fallecidos por pasajeros cada 1.000.000",
    xaxis_title="Año",
    yaxis_title="Fallecidos",
)

col1.plotly_chart(fig_ratio_passengers, use_container_width=True, width= 1000)

data_5years = pd.read_csv("https://raw.githubusercontent.com/perico3372/proyecto_individual_2/main/pages/dataframe_5years.csv")

####################################
##Fallecidos/Cantidad de pasajeros##
####################################

diff_value_ratio_passengers_5years = np.diff(data_5years["ratio_passengers"], prepend=0)

# Crear el gráfico de cascada con plotly

fig_ratio_passengers_5years = go.Figure(go.Waterfall(
    name="",
    orientation="v",
    x=data_5years['year_interval'].astype(str),
    y=diff_value_ratio_passengers_5years,
    textposition="inside",
    #text=df['Valor'],
    connector={"line": {"color": "rgb(63, 63, 63)"}},
))

# Crear el gráfico de líneas

x_line = data_5years['year_interval']
y_line = data_5years["ratio_passengers"]
fig_ratio_passengers_5years.add_trace(go.Scatter(
    x=x_line,
    y=y_line,
    mode='lines',
    name='Línea',
    ))
    
    # Personalizar el gráfico
fig_ratio_passengers_5years.update_layout(
    title="Ratio fallecidos por cada 1.000.000 de pasajeros",
    xaxis_title="Lustro",
    yaxis_title="cantidad accidentes por año",
)

col2.plotly_chart(fig_ratio_passengers_5years, use_container_width=True, width= 1000)

####################################
##Fallecidos/Cantidad de pasajeros##
####################################


limite_inferior_ratio_accidents = st.slider("Definir limite in(Año)", 1969, 1980, 2021)
data_ratio_accidents = data[data['year'] > limite_inferior_ratio_accidents]
diff_value_ratio_accidents = np.diff(data_ratio_accidents["ratio_fligts"], prepend=0)

# Crear el gráfico de cascada con plotly

fig_ratio_passengers = go.Figure(go.Waterfall(
    name="",
    orientation="v",
    x=data_ratio_accidents['year'].astype(str),
    y=diff_value_ratio_accidents,
    textposition="inside",
    #text=df['Valor'],
    connector={"line": {"color": "rgb(63, 63, 63)"}},
))

# Crear el gráfico de líneas

x_line = data_ratio_accidents['year']
y_line = data_ratio_accidents["ratio_fligts"]
fig_ratio_passengers.add_trace(go.Scatter(
    x=x_line,
    y=y_line,
    mode='lines',
    name='Línea',
    ))
    
    # Personalizar el gráfico
fig_ratio_passengers.update_layout(
    title={
    'text': "Ratio (Fallecidos / Cantidad de pasajeros)* 1.000.000",
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'
},
    xaxis_title="Año",
    yaxis_title="cantidad accidentes por año",
)

col1.plotly_chart(fig_ratio_passengers, use_container_width=True, width= 1000)

####################################
##Fallecidos/Cantidad de pasajeros##
####################################

diff_value_ratio_accidents_5years = np.diff(data_5years["ratio_fligts"], prepend=0)

# Crear el gráfico de cascada con plotly

fig_ratio_passengers_5years = go.Figure(go.Waterfall(
    name="",
    orientation="v",
    x=data_5years['year_interval'].astype(str),
    y=diff_value_ratio_accidents_5years,
    textposition="inside",
    #text=df['Valor'],
    connector={"line": {"color": "rgb(63, 63, 63)"}},
))

# Crear el gráfico de líneas

x_line = data_5years['year_interval']
y_line = data_5years["ratio_fligts"]
fig_ratio_passengers_5years.add_trace(go.Scatter(
    x=x_line,
    y=y_line,
    mode='lines',
    name='Línea',
    ))
    
    # Personalizar el gráfico
fig_ratio_passengers_5years.update_layout(
    title={
    'text': "Ratio (Fallecidos / Cantidad de pasajeros)* 1.000.000",
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'
},
    xaxis_title="Año",
    yaxis_title="cantidad accidentes por año",
)

col2.plotly_chart(fig_ratio_passengers_5years, use_container_width=True, width= 1000)
