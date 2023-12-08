import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parámetros de la distribución normal
media = 0  # Media
desviacion_estandar = 1  # Desviación estándar

# Generar datos para la distribución normal
datos = np.random.normal(media, desviacion_estandar, 1000)

# Calcular la función de densidad de probabilidad (pdf) teórica
x = np.linspace(-4, 4, 100)
pdf_teorica = norm.pdf(x, media, desviacion_estandar)

# Graficar el histograma de los datos y la pdf teórica
plt.hist(datos, bins=30, density=True, alpha=0.7, label='Datos')
plt.plot(x, pdf_teorica, label='PDF Teórica', color='red')
plt.title('Distribución Normal de Frecuencias')
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.show()
