#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 14:53:21 2023

@author: pablo
"""


import os
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pandas as pd
from pyspark.sql import SparkSession
import streamlit as st
import matplotlib.pyplot as plt

import plotly.graph_objects as go

    
spark = SparkSession.builder.getOrCreate()

dataframe_final = spark.read.csv("/_disk_dev/spyder/pages/dataframe_final.csv", header=True, inferSchema=True)
data = dataframe_final.toPandas()

# Aplicar filtro en los datos
limite_inferior_fatalities_number = st.slider("Definir", 1970, 1980, 2021)
fatalities_number = data[data['year'] > limite_inferior_fatalities_number]

diff_fatalities_number = np.diff(fatalities_number["num_accidents"], prepend=1)

# Crear el gráfico de cascada con plotly
fig_fatalities_number = go.Figure(go.Waterfall(
    name="",
    orientation="v",
    x=fatalities_number['year'].astype(str),
    y=diff_fatalities_number,
    textposition="inside",
    #text=df['Valor'],
    connector={"line": {"color": "rgb(63, 63, 63)"}},
))


x_line = fatalities_number['year']
y_line = fatalities_number["num_accidents"]
fig_fatalities_number.add_trace(go.Scatter(
    x=x_line,
    y=y_line,
    mode='lines',
    name='Línea',
    ))



# Personalizar el gráfico
fig_fatalities_number.update_layout(
    title={
    'text': "Evolución de la cantidad de fallecidos por año",
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'
},
    xaxis_title="Año",
    yaxis_title="Fallecidos",
)


st.plotly_chart(fig_fatalities_number)