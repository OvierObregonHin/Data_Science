# Importamos la biblioteca numpy para realizar cálculos numéricos
import numpy as np

# Creamos un conjunto de datos de ejemplo
datos = [15, 22, 18, 25, 30, 12, 20]

# Calculamos los cuartiles utilizando numpy
q1 = np.percentile(datos, 25)  # Primer cuartil (Q1)
q3 = np.percentile(datos, 75)  # Tercer cuartil (Q3)

# Calculamos el rango intercuartílico (RIC)
ric = q3 - q1

# Mostramos los resultados
print("Datos:", datos)
print("Primer cuartil (Q1):", q1)
print("Tercer cuartil (Q3):", q3)
print("Rango Intercuartílico (RIC):", ric)
