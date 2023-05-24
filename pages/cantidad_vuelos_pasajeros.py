#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/perico3372/proyecto_individual_2/main/pages/dataframe_final.csv")

################################################
##Cantidad de vuelos y pasajeros transportados##
################################################

# Aplicar filtro en los datos
limite_inferior_passengers = st.slider("Definir limite inferior(Año)", 1970, 1980, 2021)
filtered_data = data[data['year'] > limite_inferior_passengers]

# Obtener los valores para los ejes x, y1 y y2
x = filtered_data['year']
y1 = filtered_data['flights']
y2 = filtered_data['total_passengers']

# Crear los trazados de las líneas
trace1 = go.Scatter(x=x, y=y1, name='Vuelos', yaxis='y1')
trace2 = go.Scatter(x=x, y=y2, name='Pasajeros', yaxis='y2')

# Crear el gráfico combinado con subtramas
fig = go.Figure(data=[trace1, trace2])

# Personalizar los ejes y el diseño del gráfico
fig.update_layout(
    title={
    'text': "Evolución de la cantidad de vuelos y pasajeros transportados",
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'
},
    
    xaxis=dict(title="Año"),
    yaxis=dict(title="Vuelos", side='left', showgrid=False),
    yaxis2=dict(title="Pasajeros", side='right', overlaying='y', showgrid=False)
)


st.plotly_chart(fig)
