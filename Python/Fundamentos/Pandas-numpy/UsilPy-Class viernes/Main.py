import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.tree import export_graphviz

data = pd.read_csv("DataTest.csv", encoding="ISO-8859-1")

columnas = data.columns.tolist()

variables = columnas[:4]
objetivo = columnas[4]

print(variables)
print(objetivo)

data["entrenamiento"] = np.random.uniform(0,1,len(data)) <= 0.7

train,test = data[data["entrenamiento"]==True], data[data["entrenamiento"]== False]

arbol = dtc(criterion="entropy",min_samples_split=20, random_state=99)
arbol.fit(train[variables], train[objetivo])

prediccion = arbol.predict(test[variables])

print(pd.crosstab(test[objetivo],prediccion, rownames=["Real"], colnames=["Prediccion"]))

with open("arbol.dot", "w") as arbDot:
    export_graphviz(arbol, out_file=arbDot, feature_names=variables)
    arbDot.close()