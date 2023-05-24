#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 10:02:08 2023

@author: pabloPerez
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pandas as pd
from pyspark.sql import SparkSession
import streamlit as st
if st.checkbox("mostrar texto"):
    st.write("Hola")
    
spark = SparkSession.builder.getOrCreate()
#dataframe_final = pd.read_csv("dataframe_final.csv")
dataframe_final = spark.read.csv("/_disk_dev/spyder/pages/dataframe_final.csv", header=True, inferSchema=True)

dataframe_final.orderBy("year").limit(3).pandas_api()
if st.checkbox("Mostrar dataframe_final"):
    st.dataframe(dataframe_final)
    
   #%% 
    

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Crear un DataFrame con los datos del gráfico de cascada
data = {
    'Categoría': ['Ingresos', 'Costos', 'Ganancias', 'Impuestos'],
    'Valor': [5000, -3000, 2000, -1000]
}
df = pd.DataFrame(data)

# Calcular los valores acumulados
df['Acumulado'] = df['Valor'].cumsum()

# Crear el gráfico de cascada con plotly
fig = go.Figure(go.Waterfall(
    name="",
    orientation="v",
    x=df['Categoría'],
    y=df['Valor'],
    textposition="inside",
    text=df['Valor'],
    connector={"line": {"color": "rgb(63, 63, 63)"}},
))

# Personalizar el gráfico
fig.update_layout(
    title="Gráfico de Cascada",
    xaxis_title="Categoría",
    yaxis_title="Valor",
)

st.pyplot(fig)
