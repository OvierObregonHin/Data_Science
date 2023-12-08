import numpy as np 

#Creamos datos 
datos = [15, 22, 18, 25, 30, 12, 20]

#calculamos los cuartiles utilizando numpy 
q1 = np.percentile(datos, 25) #Primer cuartil (Q1)
q2 = np.percentile(datos, 50) #segundo cuartil (Q2)
q3 = np.percentile(datos, 75) #Tercer cuartil (Q3)

#Mostramos resultados 
print("datos: ", datos)
print("Primer cuartil (Q1): ", q1)
print("Segundo cuartil (Q2): ", q2)
print("Tercer cuartil (Q3): ", q3)

