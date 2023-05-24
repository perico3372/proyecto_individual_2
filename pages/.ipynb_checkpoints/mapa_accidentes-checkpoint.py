#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:52:29 2023

@author: pablo
"""

import os
import pandas as pd
import streamlit as st

# Obtener el directorio actual del archivo
current_dir = os.path.dirname(os.path.abspath(__file__))

# Leer el archivo CSV
data_aviation = pd.read_csv(os.path.join(current_dir, 'aviation.csv'))




limite_inferior_aviation = st.slider("Definir limite inferior(años)", 1970, 1980, 2021)
filtered_data = data_aviation[data_aviation['year'] > limite_inferior_aviation]


st.write(filtered_data)