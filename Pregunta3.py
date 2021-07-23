#Jacobi
'''El sistema de ecuaciones por resolver es el siguiente:
7x1+x2-x3+2x4=3
x1+8x2+0x3-2x4=-5
-x1+ox2+4x3-x4=4
2x1-2x2-x3+6x4=-3

'''
#Definiendo las ecuaciones a resolver
#en forma diagonalmente dominante
print("\n\n\tMetodo de Jacobi\n")
f1 = lambda a, b, c, d: (3 - b - c - 2*d)/7
f2 = lambda a, b, c, d: (-5 - a - 0*c + 2*d)/8
f3 = lambda a, b, c, d: (4 + a - 0*b + d)/4
f4 = lambda a, b, c, d: (-3 - 2*a + 2*b + c)/6

#Valores Iniciales
a0 = 0
b0 = 0
c0 = 0
d0 = 0
count = 1

#Error de Tolerancia
e = float(input('Ingrese valor de tolerancia: '))

#Implementación de la Iteración de Jacobi
print('\nn\t\ta\t\t\tb\t\t\tc\t\t\td\n')

condition = True

while condition:
    a1 = f1(a0, b0, c0, d0)
    b1 = f2(a0, b0, c0, d0)
    c1 = f3(a0, b0, c0, d0)
    d1 = f4(a0, b0, c0, d0)

    print('%d\t%0.4f\t%0.4f\t%0.4f\t%0.4f\n' % (count, a1, b1, c1, d1))
    e1 = abs(a0 - a1);
    e2 = abs(b0 - b1);
    e3 = abs(c0 - c1);
    e4 = abs(d0 - d1);

    count += 1
    a0 = a1
    b0 = b1
    c0 = c1
    d0 = d1

    condition = e1 > e and e2 > e and e3 > e

print('\nEsta es una buena aproximación: a=%0.3f, b=%0.3f, c=%0.3f y d=%0.3f\n' % (a1, b1, c1 , d1))



#Gauss-Seidel
print("\n\tMetodo de gauss-Seidel\n")
import numpy
m=int(input("Ingrese número de filas: "))
n=int(input("Ingrese número  de columnas: "))
matrix = numpy.zeros((m,n))
x=numpy.zeros((m))

vector= numpy.zeros((n))
comp=numpy.zeros((m))
error=[]

print("Introduce la matriz y el vector solución")
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Ingrese elemento a["+str(r+1)+","+str(c+1)+"]: "))
    vector[(r)]=float(input('b['+str(r+1)+']: '))
tol=float(input("Indique la tolareancia: "))
itera=int(input("Indique un numero de iteraciones: "))
print("\nLa matriz planteada es\n\n")
print(matrix)
print(vector)
print()
k=0
while k<itera:
    suma=0
    k=k+1
    for r in range(0,m):
        suma=0
        for c in range(0,n):
            if(c!=r):
                suma=suma+matrix[r,c]*x[c]
        x[r]=(vector[r]-suma)/matrix[r,r]
        print("x["+str(r)+"]: "+str(x[r]))
    del error[ : ]

    for r in range(0,m):
        suma=0
        for c in range(0,n):
            suma=suma+matrix[r,c]*x[c]
        comp[r]=suma
        dif=abs(comp[r]-vector[r])
        error.append(dif)
        print("\nError en x[",r,"]= ",error[r])
    print("\nIteraciones: ",k)
    if all ( i<=tol for i in error) ==True:
        break




