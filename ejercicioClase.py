#!/bin/python3
# 1) Indica que numero es mayor que el otro
#2) Imprimir los numeros entre medio 



numElementos= int(input("Cuantos elementos quieres?: "))

lista= []

for i in range(0,numElementos):
     numero = int(input("Introduce el número:  "))
     lista.append(numero)

# print(lista)

# num1 = int(input("Introduce el numero 1: "))
# num2 = int(input("Introduce el numero 2:"))
 
# if num2 < num1:
#     print("El numero 1 es mayor que el numero 2")
#     for nuemro in range(num2, num1+1):
#         print(nuemro)

# else:
#     print("El numero 2 es mayor que el numero 1")
#     for nuemro in range(num1, num2+1):
#         print(nuemro)


#El for cuando no tienen nada que iterar
#Cuenta instagram python

#3) Media de los 2 numeros

# print(float((num1 + num2)/ 2))

#4) Usuario elige elementos y nuemros que hayan en la lista

#Calcular media lista


# print("La media de los numeros de la lista es: ", sum(lista) / len(lista))

#Numero al buscar en la lista



numUsuario = int(input("Introduce un numero que quieres buscar en la lista: "))

if (numUsuario in lista):
    print("El numero esta en la posición:", lista.index(numUsuario))
else:
    print("El numero no esta en la lista")










#Ordenacion de la lista

lista.sort()
print(lista)

print(repr(enumerate(lista)))
#Ordenar 2 listas y juntarlas en una

lista1 = [1,2,5,2,6,5,6]
lista2 = [5,8,54,3,5,3]

lista1.sort; lista2.sort

unionLista = lista1 + lista2

