#Sustitución progresiva
import numpy as np
print("\n\tSustitución Progresiva")
'''La ecuación planteada es la siguiente:
 6x1                      =12
 3x1+6x2               =-12
 4x1-2x2+7x3         =14
 5x1-3x2+9x3+21x4=-2
'''

A = np.array([[6,0,0,0], [3,6,0,0],  [4,-2,7,0],  [5,-3,9,21]])

B = np.array([[12], [-12],  [14],  [-2]])


c = 1e-15
# Evitar truncamiento
A = np.array(A, dtype=float)
AB = np.concatenate((A, B), axis=1)
AB0 = np.copy(AB)

# Pivoteo parcial por filas
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

# Para cada fila en AB
for i in range(0, n - 1, 1):
    columna = abs(AB[i:, i])
    dondemax = np.argmax(columna)

    if (dondemax != 0):
        temporal = np.copy(AB[i, :])
        AB[i, :] = AB[dondemax + i, :]
        AB[dondemax + i, :] = temporal
AB1 = np.copy(AB)

# eliminación progresiva
for i in range(0, n - 1, 1):
    pivote = AB[i, i]
    adelante = i + 1
    for k in range(adelante, n, 1):
        factor = AB[k, i] / pivote
        AB[k, :] = AB[k, :] - AB[i, :] * factor

# sustitución recursiva
ultfila = n - 1
ultcolumna = m - 1
X = np.zeros(n, dtype=float)

for i in range(ultfila, 0 - 1, -1):
    suma = 0
    for j in range(i + 1, ultcolumna, 1):
        suma = suma + AB[i, j] * X[j]
    b = AB[i, ultcolumna]
    X[i] = (b - suma) / AB[i, i]

X = np.transpose([X])

print('\nLa matriz planteada es:')
print(AB0)
print('\nSe aplica pivoteo parcial por filas')
print(AB1)
print('Eliminación progresiva')
print(AB)
print('El resultado de la matriz propuesta es: ')
print(X)


#Factorización LU
'''Cabe decri que en este caso solo mostrareomos tanto la matriz U como la matriz L,
Dado que el resultado ya sale en el primer codigo ademas,
 se vizualiza en el archivo de latex'''
import numpy as np
print("\n\n\tDescomposición LU")
m=int(input("Introduce el tamaño de tu matriz: "))
matriz=np.zeros([m,m])
u=np.zeros([m,m])
l=np.zeros([m,m])
print("Ingresa los elementos: ")
for r in range(0,m):
    for c in range(0,m):
        matriz[(r),(c)]=(input("Ingrese elemento a["+str(r+1)+","+str(c+1)+"]: "))
        matriz[(r), (c)] = float(matriz[(r),(c)])
        u[(r), (c)]= matriz[(r),(c)]

for k in range(0,m):
    for r in range (0,m):
        if (k==r):
            l[(k),(r)]=1
        if (k<r):
            factor=(matriz[(r),(k)]/matriz[(k),(k)])
            l[(r),(k)]=factor
            for c in range (0,m):
                matriz[(r),(c)]=matriz[(r),(c)]-(factor*matriz[(k),(c)])
                u[(r), (c)] = matriz[(r), (c)]
print("\nResultados\n")
print("\nMatriz L\n")
print(l)
print("\nMatriz U\n")
print(u)

