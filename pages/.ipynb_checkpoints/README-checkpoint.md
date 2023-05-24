Consideraciones iniciales

Inicie el analisis a partir de la década del '70.
Hice segmento analisis en lustro para obtener una vision mas amplia. 
Para efectuar el EDA utilice la libreria pandas-profiling y dtale.
Utilice para hacer ETL basicamente los modulos de pyspark una herramienta, ami parecer mucho mas potente que pandas pero un poco más compleja en su uso. Herramienta utilizada en lenguaje python tanto como en scala.
Para el dashboard utilice streamlit.

Durante el trabajo de EDA de la base de datos pude deducir que el campo ground eran fallecidos en tierra firme al listar outliers, pude visualizar que tenía un valor mayor a 5000 en el año 2001, el año del atententado al Worl Trade Center.
Observado la base de datos pude ver que Estados Unidos de America no aparecía como pais, pero si sus estados debí hacer un reemplazo de los valores.




Conclusiones:

Desde la principios de la decada del '70 se producido un marcado descenso del ratio de pasajeros transportados respecto del numero de fallecidos por accidentes aereos. Asi comno el ratio de cantidad de vuelos respecto de la cantidad de accidentes. Hay algunas excepciones por ejemplo en año 1.972 donde podemos encontrar el accidente aéro de la cordillera de los Andes en los que involucró al seleccionado de Rugby de Ururguay.
El numero de accidentes disminuyó como el número de fallecidos, en los últimos 50 años.


