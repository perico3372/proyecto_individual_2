#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:01:23 2023

@author: pablo
"""

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

dataframe_final = spark.read.csv("/_disk_dev/spyder/pages/dataframe_5years.csv", header=True, inferSchema=True)
data_5years = dataframe_final.toPandas()



diff_fatalities_number_5years = np.diff(data_5years["num_accidents"], prepend=1)

# Crear el gráfico de cascada con plotly
fig_fatalities_number_5years = go.Figure(go.Waterfall(
    name="",
    orientation="v",
    x=data_5years['year_interval'].astype(str),
    y=diff_fatalities_number_5years,
    textposition="inside",
    #text=df['Valor'],
    connector={"line": {"color": "rgb(63, 63, 63)"}},
))


x_line = data_5years['year_interval']
y_line = data_5years["num_accidents"]
fig_fatalities_number_5years.add_trace(go.Scatter(
    x=x_line,
    y=y_line,
    mode='lines',
    name='Línea',
    ))



# Personalizar el gráfico
fig_fatalities_number_5years.update_layout(
    title={
    'text': "Evolución de la cantidad de fallecidos por lustro",
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'
},
    xaxis_title="Año",
    yaxis_title="Fallecidos",
)


st.plotly_chart(fig_fatalities_number_5years)