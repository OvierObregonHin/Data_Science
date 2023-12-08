# Creamos un conjunto de datos de ejemplo
datos = [15, 22, 18, 25, 30, 12, 20]

# Ordenamos el conjunto de datos
datos_ordenados = sorted(datos)

# Calculamos la mediana
n = len(datos_ordenados)
if n % 2 == 1:
    # Si la longitud es impar, la mediana es el valor en el medio
    mediana = datos_ordenados[n // 2]
else:
    # Si la longitud es par, la mediana es el promedio de los dos valores centrales
    mediana = (datos_ordenados[(n // 2) - 1] + datos_ordenados[n // 2]) / 2

# Mostramos el resultado
print("Datos:", datos)
print("Mediana:", mediana)
