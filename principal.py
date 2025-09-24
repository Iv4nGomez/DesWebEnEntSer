#Listas: Guardar una serie de datos que SI se pueden repetir y que puden tener diferentes tipos de datos. 
#Y una vez creado se puede modificar ya que es mutable.

#Crear una lista vacia
lista = []
print(lista)

#Crear una lista con datos
lista2 = [1, "ivan", 20.5, False] 
print(lista2)

#Tambien se puede crear una lista con el constructor list()
lista3 = list([1, "ivan", 20.5, False]) #Puedes meter dentro como parametro por ejemplo una lista
print(lista3)

#Pero puedes poner también otro tipos de datos y pasa esto
lista4 = list("ivan")
lista5 = list("1 2 3 4 5 6 7 8 9 0") #Itera en las cadenas de texto todo los caracteres, incluidos los espacios
print(lista4) 
print(lista5)

print(lista4[-2]) #Si ponemos un indice negativo empieza a contar desde el final de la lista

#Como funcionan los slice en las listas

#Señalar el comienzo y el final
print(lista4[0:3]) #No incluye el indice 3
#Señalar solo el comienzo hasta el final
print(lista4[2:])
#Señalar el final solo
print(lista4[:3])
#Señalar todo
print(lista4[:])
#Igual que el primero pero con step
print(lista4[0:4:2]) 
#También se puede hacer con indices negativos todo lo anterior
print(lista4[-4:-1]) #Esto no llegaría al final ya que no el -1 no se incluye

#funciones propias de las listas
#Para ver la longitud de una lista
print(len(lista4))
#El máximo y el minimo valor de una lista
print(max(lista4)) 
print(min(lista4)) 
print(max(lista5))
#Sumar todos los valores de una lista

#print(sum(lista4)) #No se puede sumar una lista de strings
#print(sum(lista5))

print(sum([1,2,3,4,5,6,7,8,9,0])) #Si se puede sumar una lista de numeros

#Ordenar una lista
lista6 = [5,3,8,1,4]
print(sorted(lista6)) 
print(lista6) #No modifica la lista original

#Ordena de mayor a menor añadiendo el parametro reverse=True a la función sorted
print(sorted(lista6, reverse=True))

#Se pueden enumerar las secuencias con la función enumerate

alumnosDeLaClase = ["ivan", "carlos", "ismael", "miguel"]

print(list((enumerate(alumnosDeLaClase)))) #Enumera la posición de cada elemento de la lista

#Pero podemos modificar el indice de comienzo de esta manera

print(list((enumerate(alumnosDeLaClase, start=200)))) #Empieza a enumerar desde el numero que pongamos en start

#Ejemplo de la propiedad mutable de las listas

lista7 = [1,2,3,4,5]
print(lista7)
lista7[0] = 100
print(lista7) 
del lista7[0] #Borra el elemento de la posición 0
print(lista7)

lista8 = [1,2,3,4,5,6,7,8,9,10]
print(lista8)
lista7 = lista8
print(lista7)
print(lista8)

#Copiar listas

lista9 = [1,2,3,4,5,6,7,"hola",9,10]
lista10 = lista9[:] #Copia toda la lista
print(lista10)
lista10[0] = 999;
print(lista10) #Si se modifica la copia de la lista
print(lista9) #No se modifica la lista original

lista11 = list(lista9)

lista12 = lista9.copy() 

#Listas dentro de listas(Multidimensionales)

tabla = [[1,2,3],[4,5,6],[7,8,9]]
print(tabla[0][0]) #Primer corchete la fila y el segundo el elemento de esa fila

#Recorrer una lista multidimensional con bucles for anidados
print("Tabla:")
for fila in tabla:
    for columna in fila:
        print(columna, end=" ")
    print() #Genera un salto de linea

#Más metodos de las listas

#Inserción

lista13 = [1,2,3,2,5]
lista13.append(6) #Añade un elemento al final de la lista
print(lista13)

lista13.extend([7,8,9]) #Añade varios elementos al final de la lista
print(lista13)

lista13.insert(0, 100) #Añade un elemento en la posición que le digamos y desplaza el resto de elementos a la derecha
print(lista13)

#Eliminar elementos

lista13.pop() #Elimina el último elemento de la lista
print(lista13)
lista13.pop(0) #Elimina el elemento de la posición que le digamos
print(lista13)
lista13.remove(8) #Elimina la primera aparición del elemento que le digamos
print(lista13)

#Ordenar

lista13.reverse() #Invierte el orden de la lista
print(lista13) #Invierte la lista original, tener en cuenta

lista13.sort() #Ordena la lista de menor a mayor
print(lista13)

lista13.sort(reverse=True) #Ordena la lista de mayor a menor
print(lista13)

#Con cadenas de texto

alumnosDeLaClase[0] = "Iván"

alumnosDeLaClase.sort() #Ordena alfabeticamente
print(alumnosDeLaClase)

alumnosDeLaClase.sort(key=str.lower) #Ordena alfabeticamente sin tener en cuenta mayusculas y minusculas
print(alumnosDeLaClase)

#Busqueda

lista14 = [5,1,1,1,1,1,10,23]
print(lista14.count(1)) #Cuenta los numeros de veces que aparece el elemento pasado por parámetro

print(lista14.index(1)) #Devuelve la posición del elemento pasado por parámetro, si hay varios devuelve el primero
print(lista14.index(1,1)) #Devuelve la posición del elemento pasado por parámetro, pero empezando a buscar desde la posición 1
print(lista14.index(1,1,3)) #Devuelve la posición del elemento pasado por parámetro, pero empezando a buscar desde la posición 1 y hasta la posición 4 (no incluida)
#print(lista14.index(5,1,3)) #Si no encuentra el elemento da error

#EJERCICIO: 

# Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo.
# Muestra el máximo de los números guardado en la lista, muestra los números pares.


# numerosUsuarios = []

# numerosUsuarios.append((int(input("Introduce numeros, si quieres parar introduce un numero negativo:"))))

# while numerosUsuarios[-1] >= 0:
#     numerosUsuarios.append((int(input("Introduce numeros, si quieres parar introduce un numero negativo:"))))

# print("El numero máximo es: ", max(numerosUsuarios))
# print("Los numeros pares son: ", )

# for numero in numerosUsuarios:
#     if numero % 2 == 0:
#         print(numero, end=" ")

#Realizar un programa que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida.
#Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].

listaString = ["Hola", "como", "estás", "espero", "que", "bien"]

listaString.reverse()

print(listaString)

#O de la siguiente manera

listaString2 = ["Soy", "el", "mejor", "programador", "del", "mundo"]

print(listaString2[::-1]) #Esta froma lo que hace pues es ir para atrás gracias a los step negativos

# Dada una lista de cadenas, pide una cadenena por teclado e indica si está en la lista, indica cuantas veces aparece en la lista, 
# lee otra cadena y sustituye la primera por la segunda en la lista, 
# y por último borra la cadena de la lista

# listaDeCadenas = ["hola", "adios", "hola", "hola", "buenos", "dias"]

# cadena = input("Introduce una cadena: ")

# if cadena in listaDeCadenas:
#     print("La cadena está en la lista") 
# else:
#     print("La cadena no está en la lista")

# print("La cadena aparece", listaDeCadenas.count(cadena), "veces")

# cadena2 = input("Cadena a reemplazar:")
# apariciones = listaDeCadenas.count(cadena)
# pos = 0

# for i in range(0,apariciones):
# 	pos = listaDeCadenas.index(cadena,pos)
# 	listaDeCadenas[pos] = cadena2
# print(listaDeCadenas)

# Dado una lista, hacer un programa que indique si está ordenada o no.

listaNumeros = [5,4,4,1,9,1,3,2,1]

listaNumerosAux = listaNumeros[:]

listaNumeros.sort()

if listaNumeros == listaNumerosAux:
    print("La lista está ordenada")
else:
    print("La lista no está ordenada")

#Map: Ejecutar funciones sobre secuencias

lista = [1,2,3,4,5,6,7,8,9,10]

def multiplicarPorDiez(numero):
    return numero * 10

print(list(map(multiplicarPorDiez, lista))) 

#Filter: Filtrar elementos de una secuencia que den true

lista = [1,2,3,4,5,6,7,8,9,10]
def esPar(numero):
    return numero % 2 == 0

print(list(filter(esPar, lista)))

 #Reduce: Devuelve un único valor a partir de una secuencia

from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]
def sumarTodaLaLista(num1, num2):
    return num1 + num2

print(reduce(sumarTodaLaLista, lista)) #Va sumando los numeros de la lista acumulandolos en un unico valor

#list comprehension

#Crear una lista fácilmente a partir de expresiones

print([x * 25 for x in [1,2,3,4,5]]) #Crea una lista con los numeros del 1 al 9 multiplicados por 10
print([x for x in range(10) if x % 2 == 0]) #Lista con los numeros pares del 0 al 9
print([x + y for x in [1,2,3] for y in [4,5,6]]) #Combina 2 listas el primer elemento se suma a todos los elementos de la segunda lista y así sucesivamente

#Tuplas: Es como una lista pero inmutable, es decir, no se puede modificar una vez creado.
#Empaquetado
tupla = (1,2,3,4,5,5)
tupla2 = 1,2,3,4,5,5 #También se puede crear sin paréntesis
tupla3 = tuple([1,2,3,4,5,5]) #También se puede crear con el constructor tuple()
print(tupla)

#Desempaquetado de tuplas
# a,b,c = tupla  #Esto da error ya que hay 6 elementos y solo 3 variables
# print(a)

# Pero se puede hacer esto para estas ocaciones
a,b,c, *resto = tupla #El operador * indica que el resto de elementos se guarden en la variable resto en una lista 
print(a)
print(b)
print(c)
print(resto)

#Podemos recorrer tuplas

for elemento in tupla:
    print(elemento, end=" ")


# Si esta un elemento en la tupla o no
print(3 in tupla)

#Podemos concatenar tuplas
tupla4 = tupla + (6,7,8) 
print (tupla4)

#Repetir tuplas
tupla5 = tupla * 3
print(tupla5)

#Mirar posiciones en concreto
print(tupla4[0])

#Y hacer slices
print(tupla4[0:3])

#Y también funciones que habiamos visto en las listas como len, max, min, sum, sorted, enumerate

#ESTO NO SE PUEDE HACER YA QUE LAS TUPLAS SON INMUTABLES
# tupla4[0] = 100

#Y los metodos de busqueda como count e index funcionan en esta estructura de datos

#Range: Sirve para crear secuencias de números enteros, es inmutable, es muy útil para reccorer con bucles

rango = range(0,10,2) #Empieza en 0, termina en 10 (no incluido) y va de 2 en 2
print (list((rango))) #Hay que convertirlo a lista para verlo
print(type(rango))

#Ejemplo de uso con bucle for
for numero in range(0,10,2):
    print(numero, end=" ")

# #Los rangos se pueden recorrer.
# Operadores de pertenencia: in y not in.
# Indexación
# Slices 
#Y también funciones que habiamos visto en las listas como len, max, min, sum, sorted, enumerate

#COMO EN LAS TUPLAS NO SE PUEDE MODIFICAR

#Podemos con .start y .stop ver el inicio y el final del rango y .step el incremento
print()
print(rango.start)
print(rango.stop)  
print(rango.step)