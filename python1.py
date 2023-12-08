import numpy as np

#Creamos un conjunto de datos de ejemplo 
datos = [15, 22, 18, 25, 30, 12, 20]

rango = np.max(datos) - np.min(datos)

#Mostramos el resultado 
print("Datos:", datos)
print("Rango", rango)
