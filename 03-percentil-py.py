import numpy as np 

#Creamos los datos 
data = [15, 22, 18, 25, 30, 12, 20]

#definimos el precenmtil que queremos 
percentil_70 = np.percentile(data, 70)

#mostramos el resultado 
print("Datos: ", data)
print("Percentil 70: ", percentil_70)
