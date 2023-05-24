#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 11:40:14 2023

@author: pablo
"""

import os
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pandas as pd
from pyspark.sql import SparkSession
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

    
spark = SparkSession.builder.getOrCreate()

dataframe_final = spark.read.csv("/_disk_dev/spyder/pages/dataframe_5years.csv", header=True, inferSchema=True)
data_5years = dataframe_final.toPandas()


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
    xaxis_title="Año",
    yaxis_title="cantidad accidentes por año",
)

st.plotly_chart(fig_ratio_passengers_5years)