import statistics 
import numpy as np 

#creamos un conjunto de datos de ejmplo 
datos = [15, 22, 18, 25, 30, 12, 20, 25, 18, 22]


#Calculamos la moda utilizando la funcion mode de statistics 
moda1 = statistics.mode(datos)
moda2 = np.argmax(np.bincount(datos))

print("Datos: ", datos)
print("Moda: ", moda1)
print("Moda: ", moda2)

