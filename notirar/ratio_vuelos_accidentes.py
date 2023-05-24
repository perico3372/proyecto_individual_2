#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 12:14:23 2023

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

dataframe_final = spark.read.csv("/_disk_dev/spyder/pages/dataframe_final.csv", header=True, inferSchema=True)
data = dataframe_final.toPandas()


####################################
##Fallecidos/Cantidad de pasajeros##
####################################


limite_inferior_ratio_accidents = st.slider("Definir limite inferior(Año)", 1969, 1980, 2021)
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

st.plotly_chart(fig_ratio_passengers)