import matplotlib.pyplot as plt
from scipy.stats import binom

# Parámetros de la distribución binomial
n = 10  # Número total de ensayos
p = 0.5  # Probabilidad de éxito en cada ensayo

# Generar valores de x (número de éxitos) para la distribución binomial
x = range(n+1)

# Calcular las probabilidades para cada valor de x
probabilidades = binom.pmf(x, n, p)

# Mostrar el resultado
print("Valores de x:", list(x))
print("Probabilidades:", probabilidades)

# Graficar la distribución binomial
plt.bar(x, probabilidades, align='center', alpha=0.7)
plt.title('Distribución Binomial')
plt.xlabel('Número de Éxitos')
plt.ylabel('Probabilidad')
plt.show()
