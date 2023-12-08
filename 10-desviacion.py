import math

# Parámetros de la distribución binomial
n = 10  # Número total de ensayos
p = 0.5  # Probabilidad de éxito en cada ensayo

# Calcular la desviación estándar
desviacion_estandar = math.sqrt(n * p * (1 - p))

# Mostrar el resultado
print("Desviación Estándar:", desviacion_estandar)
