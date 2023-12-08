# Importamos la biblioteca numpy para realizar cálculos numéricos
import numpy as np

# Creamos un conjunto de datos de ejemplo
datos = [15, 22, 18, 25, 30, 12, 20]

# Calculamos la desviación estándar utilizando numpy
desviacion_estandar = np.std(datos)

# Mostramos el resultado
print("Datos:", datos)
print("Desviación Estándar:", desviacion_estandar)
