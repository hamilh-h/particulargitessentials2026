#7. Crear un vector de 18 valores aleatorios enteros entre 1 y 50, y mostrar por pantalla el promedio de todos sus valores

import random

vector = []
for i in range(18):
    vector.append(random.randint(1, 50))

print("Vector original:")
print(vector)

suma = 0
for i in range(len(vector)):
    suma += vector[i]

mean_value = suma / len(vector)
print("El promedio de todos los valores es:", mean_value)
