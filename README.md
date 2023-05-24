# Proyecto Individual: Data Analitics

## Consideraciones iniciales

Inicie el analisis a partir de la década del '70. Debido a la incorporación de dos bases de de datos del banco mundial donde los datos iniciaban desde 1.970.
Links de las bases de datos:  
https://api.worldbank.org/v2/es/indicator/IS.AIR.DPRT?downloadformat=csv
https://api.worldbank.org/v2/es/indicator/IS.AIR.PSGR?downloadformat=csv

Hice analisis en lustro para obtener una vision mas amplia. 

Para efectuar el EDA utilice la libreria pandas-profiling y dtale.
Utilice para hacer ETL basicamente los modulos de pyspark una herramienta, a mi parecer mucho mas potente que pandas pero un poco más compleja en su uso. Herramienta utilizada en lenguaje python tanto como en scala.
Para el dashboard utilice streamlit.

Durante el trabajo de EDA de la base de datos pude deducir que el campo ground eran fallecidos en tierra firme al listar outliers, pude visualizar que tenía un valor mayor a 5000 en el año 2001, el año del atententado al Worl Trade Center.
Observando la base de datos pude ver que Estados Unidos de America no aparecía como pais, pero si sus estados debí hacer un reemplazo de los valores.

## KPI's:
Una consideración a tener en cuenta 2020 fue el año de la pandemia dónde los aeropuertos estaban cerrados, practicamente no había vuelos en cambio en el 2021 comenzó a haber más circulación.  
Reducir en 5% la tasa de letalidad a nivel anual, siendo el número de fallecidos en los accidentes aéreos respecto al total de personas en los vuelos involucrados. Se tomo del del año 2020 respecto del año 2021. No cumpliendose las expectativas planteadas para el periodo dando un 11,66% de incremento.  
Los dos primero KPI recomendados por mi se basan sobre la accidentabilidad mientras que el último sobre la letalidad.
KPI recomendados a tener en cuenta:
* La cantidad de vuelos por año respecto del número de accidentes por año, comparando año 2020 con 2021. Se plantea como objetivo un desxcenso del 5%. Dando como resultado un marcado descenso.  
* La cantidad de pasajeros por año respecto al número de fallecidos por año, realizandose la comparacion 2020 respecto 2021. Se plantea como objetivo reducir un 50% una vez analizado la evolución de este ratio.en los ultimos años habia una evolución en torno al 50-70%, excepto en el periodo 2019-2020. Obteniendose un 70,96%.
* La cantidad de fallecidos respecto de el número de accidentes, tambien se realiza la comparacion por el mismo periodo. Se planteó un KPI donde hubiese una reducción del 50%. Obteniendose valores cercanos al 60%.

# Conclusiones:

Desde la principios de la decada del '70 se producido un marcado descenso del ratio de pasajeros transportados respecto del numero de fallecidos por accidentes aereos. Asi comno el ratio de cantidad de vuelos respecto de la cantidad de accidentes. Hay algunas excepciones por ejemplo en año 1.972 donde podemos encontrar el accidente aéro de la cordillera de los Andes en los que involucró al seleccionado de Rugby de Ururguay.  
Pude observar que el numero de fallecidos en el año 1972 hubo un incremento en la tendencia que no persistió, en cual se produjeron 12 accidentes con mas de 100 decesos.
El numero de accidentes disminuyó como el número de fallecidos, en los últimos 50 años.

link dashboard : https://perico3372-proyecto-individual-2-main-20sk14.streamlit.app/

Autor: Pérez, Pablo Jorge
