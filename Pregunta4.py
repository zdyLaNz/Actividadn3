# FROBENIUS
import numpy as np
from math import sqrt
import numpy

'''
En este caso nuestro programa dar la opcion al usuarion de ingresar los datos de la matriz
 mediante teclado
'''
print("\nIntrodusca los valores que tendras su matriz:")
m=int(input("Ingrese número de filas: "))
n=int(input("Ingrese número  de columnas: "))
matrix = numpy.zeros((m,n))
#x=numpy.zeros((m))

print("Introduce la matriz y el vector solución")
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Ingrese elemento a["+str(r+1)+","+str(c+1)+"]: "))

print("\nMostrando la matriz Planteada\n")
print(matrix)
print()

def normaF(matrix):
	sum = 0
	for i in range(m):
		for j in range(n):
			sum += pow(matrix[i][j], 2)

	res = sqrt(sum)
	return round(res, 5)
print("Mostrando resultado mediante la norma Frobenius:\n")
print(normaF(matrix))