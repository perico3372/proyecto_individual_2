#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv("https://raw.githubusercontent.com/perico3372/proyecto_individual_2/main/pages/dataframe_final.csv")

#kpi fallecidos/pasajeros + tripulacion
kpi_a_2020 = (data.loc[data["year"] == 2020, 'passenger_fatalities'].values[0]+data.loc[data["year"] == 2020, 'crew_fatalities'].values[0])/(data.loc[data["year"] == 2020, 'all_aboard'].values[0])
kpi_a_2021 = (data.loc[data["year"] == 2021, 'passenger_fatalities'].values[0]+data.loc[data["year"] == 2021, 'crew_fatalities'].values[0])/(data.loc[data["year"] == 2021, 'all_aboard'].values[0])

kpi_a = (100-(kpi_a_2021 / kpi_a_2020)*100)*(-1)
kpi_a_format = f"{kpi_a:.2f}"
st.markdown("---")
st.markdown("Se plantea como objetivo un incremento del 5%")
st.write("KPI fallecidos respecto pasajeros y tripulacion a bordo en el accidente", kpi_a_format,"%")
st.markdown("ATENCION: Hubo in icremento, por lo tanto no se cumplió con el KPI")


#kpi accidentes/vuelos
kpi_b_2020 = (data.loc[data["year"] == 2020, 'num_accidents'].values[0])/(data.loc[data["year"] == 2020, 'flights'].values[0])
kpi_b_2021 = (data.loc[data["year"] == 2021, 'num_accidents'].values[0])/(data.loc[data["year"] == 2021, 'flights'].values[0])

kpi_b = 100-(kpi_b_2021 / kpi_b_2020)*100
kpi_b_format = f"{kpi_b:.2f}"
st.markdown("---")
st.markdown("Se plantea como objetivo un incremento del 5%")
st.write("Cantidad de accidentes respecto de Número de Vuelos",kpi_b_format, "%")
st.markdown("Se cumplió con el KPI")

#kpi fallecidos / pasajeros

kpi_c_2020 = (data.loc[data["year"] == 2020, 'passenger_fatalities'].values[0]+data.loc[data["year"] == 2020, 'crew_fatalities'].values[0])/(data.loc[data["year"] == 2020, 'total_passengers'].values[0])
kpi_c_2021 = (data.loc[data["year"] == 2021, 'passenger_fatalities'].values[0]+data.loc[data["year"] == 2021, 'crew_fatalities'].values[0])/(data.loc[data["year"] == 2021, 'total_passengers'].values[0])

kpi_c = 100-(kpi_c_2021 / kpi_c_2020)*100
kpi_c_format = f"{kpi_c:.2f}"

st.markdown("---")
st.markdown("Se plantea como objetivo un incremento del 50%")
st.write("Cantidad de fallecidos respecto de numero de pasajeros en todos los vuelos del año",kpi_c_format,"%")
st.markdown("Se cumplió con el KPI")
            
kpi_d_2020 = (data.loc[data["year"] == 2020, 'passenger_fatalities'].values[0]+data.loc[data["year"] == 2020, 'crew_fatalities'].values[0])/(data.loc[data["year"] == 2020, 'num_accidents'].values[0])
kpi_d_2021 = (data.loc[data["year"] == 2021, 'passenger_fatalities'].values[0]+data.loc[data["year"] == 2021, 'crew_fatalities'].values[0])/(data.loc[data["year"] == 2021, 'num_accidents'].values[0])

kpi_d = 100-(kpi_d_2021 / kpi_d_2020)*100
kpi_d_format = f"{kpi_d:.2f}"
st.markdown("---")
st.markdown("Se plantea como objetivo un incremento del 50%")
st.write("Cantidad de fallecidos respecto del número de accidentes",kpi_d_format,"%")
st.markdown("Se cumplió con el KPI")
#numero_formateado = "{:.2f}".format(numero)