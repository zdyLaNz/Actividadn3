#Pregunta 2


import numpy
import scipy
import scipy.linalg   # SciPy Linear Algebra Library
#Resolución de la primera matriz
A = numpy.array([[4, 6, 10], [6, 25, 19], [10, 19, 62]])
L = scipy.linalg.cholesky(A, lower=True)
L2 = scipy.linalg.cholesky(A, lower=False)

print("L matriz planteada es:")
print("A=")
print(A)
print("\nMostrando los resultados mediante el metodo planteado")
print("A=L*L^T")
print("L:")
print(L)
print("*L^T:")
print(L2)
print("\n")

#Resolución de la segunda matriz
B = numpy.array([[4, 6, 10], [6, 3, 19], [10, 19, 62]])
l = scipy.linalg.cholesky(B, lower=True)
l2 = scipy.linalg.cholesky(B, lower=False)

print("L matriz planteada es:")
print("B=")
print(B)
print("\nMostrando los resultados mediante el metodo planteado")
print("B=L*L^T")
print("L:")
print(l)
print("*L^T:")
print(l2)

