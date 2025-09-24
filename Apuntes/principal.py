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

#Codificaciones 
print("Codificación de caracteres:")
#ASCII: 7 bits, 128 caracteres
#ISO-8859-1: 8 bits, 256 caracteres
#Unicode: 32 bits, más de un millón de caracteres
#UTF-8: Es unicode pero los caracteres pueden ocupar un numero de bytes variable 

#Funciones ord() y chr()

#Devuelve el caracter correspondiente al código ASCII pasado por parámetro
print(chr(97))

#Ahora al revés, devuelve el código ASCII del caracter pasado por parámetro
print(ord("a"))

#Cadenas de caracteres
print("Cadenas de caracteres:")
#Definir cadenas de caracteres
cad1 = "Hola"
cad2 = 'Java me gusta menos que Python'
cad2 = '''Hola que tal espero
        que todo este bien'''

cad1 = str([1,2,3,4,5]) 
cad2 = str(4)
cad3 = str(4.5)

print(type(cad1))
print (type(cad2))
print (type(cad3))

#Las cadenas tienen las mismas propiedades que las listas y las tuplas
# Y las mismas funciones

#Son inmutables

#Comparación de cadenas
print("informatica">"informacion")

for letra in "informatica":
    print(ord(letra), end=" ")
print()
for letra in "informacion":
    print(ord(letra), end=" ")

#Es menor porque tiene un 99 en ASCII y la otra una 111 a partir de ahi ya será menor ya que va de izquierda a derecha

#Funciones repr, ascii, bin

#repr: Devuelve la representación en cadena de un objeto1

print(repr(range(10)))
print(repr("piña"))

print(type(repr("piña")))

#Si queremos que nos de la cadena pero que siga siendo del tipo objeto solo tendremos que usar la funcion eval
print(type(eval(repr(range(10))))) #Si se hace con una cadena de texto pues sera del mismo tipo

#ascii: Devuelve la cadena como la otra función pero esta vez muestra los caracteres conun codigo de escape por ejemplo á sería \xe1
print(ascii("piña"))

#bin: Le das un número entero y te devuelve su representación en binario
print(bin(2005))
# print(bin("hola")) #Da error ya que no es un entero

#Métodos principales de las cadenas de texto

cadena = "Python es el mejor lenguaje de programación"

print(cadena.capitalize()) #Pone la primera letra en mayuscula y el resto en minuscula
print(cadena.lower()) #Pone toda la cadena en minuscula
print(cadena.upper()) #Pone toda la cadena en mayuscula
print(cadena.swapcase()) #Cambia las mayusculas por minusculas y viceversa
print(cadena.title()) #Pone la primera letra de cada palabra en mayuscula
print(cadena.center(50)) #Centra la cadena en un espacio de 50 caracteres
print(cadena.center(50, "=")) #Centra la cadena en un espacio de 50 caracteres y rellena con el caracter que le digamos
print(cadena.ljust(50, "=")) #Mete la cadena a la izquierda en un espacio de 50 caracteres y rellena con el caracter que le digamos
print(cadena.rjust(50, "=")) #Mete la cadena a la derecha en un espacio de 50 caracteres y rellena con el caracter que le digamos

num = 526
print(str(num).zfill(10)) #Rellena con ceros a la izquierda hasta completar el número de caracteres que le digamos #3 + 7 ceros = 10

#Métodos de búsqueda

print(cadena.count("o")) #Cuenta las veces que aparece el caracter o la cadena pasada por parámetro
print(cadena.count("o", 3)) #Cuenta las veces que aparece el caracter o la cadena pasada por parámetro pero empezando a contar desde la posición que le digamos
print(cadena.count("o", 3, 20)) #Cuenta las veces que aparece el caracter o la cadena pasada por parámetro pero empezando a contar desde la posición que le digamos y hasta la posición que le digamos (no incluida)

print(cadena.find("Python")) #Devuelve la posición de la primera aparición del caracter o la cadena pasada por parámetro, si no lo encuentra devuelve -1
print(cadena.find("x")) #Ejemplo de que no lo encuentra

print(cadena.rfind("o")) #Devuelve la posición de la última aparición del caracter o la cadena pasada por parámetro

#index y rindex son parecidos pero no es tan adecuado para cadenas ya que da error si no lo encuentra

#Metodos de validacion

print(cadena.startswith("x")) #Devuelve True si la cadena empieza por el caracter o la cadena pasada por parámetro
print(cadena.startswith("o", 15)) #Segundo parámetro pasado es la pos de inicio
print(cadena.endswith("o")) #Si termina por el caracter o la cadena pasada por parámetro
print(cadena.endswith("o", 0, 20)) #Si termina por el caracter o la cadena pasada por parámetro entre las posiciones que le digamos. Segundo parametro inicio tercero fin (no incluido)

#Aparte de estás hay muchas mas

#Metodos de sustitución

print('{} {}'.format("a", "b")) #Sustituye los {} por los parámetros pasados en orden
print('{1} {0}'.format("a", "b")) #Sustituye los {} por los parámetros pasados en el orden que le digamos
print('{0} {1}'.format("a", "b"))

print('{nombre} {apellido}'.format(nombre="Ivan", apellido="Gomez")) #Ahora el orden se decide por el nombre como si fuera un identificador

print('{0:b} {1:x} {2:.2f}'.format(123, 223,12.2345)) #El primer parametro lo muestra en binario, el segundo en hexadecimal y el tercero con 2 decimales

print('{:^10}'.format('test')) #Centrado como en el anterior ejemplo de center pero de esta manera #El :^ indica centrado y el 10 el espacio total

#Otros metodos de sustitución

buscar = "nombre apellido"
reemplazar_por = "Iván Gómez" 

print ("Estimado Sr. nombre apellido: nombre apellido nombre".replace(buscar, reemplazar_por))  #Sustituye todas las apariciones de la cadena por la otra cadena

cadena = "  www.google.com            "
print(cadena.strip()) #Elimina los espacios en blanco al principio y al final de la cadena

cadena = "000000000000111111100000001ivan0000101"

print(cadena.strip("01")) #Elimina los caracteres que le pasemos como parametro

#Metodos de unión y división

formato_numero_factura = ("Nº 0000-0", "-0000 (ID: ", ")")
print("275".join(formato_numero_factura)) #La cadena que pasemos al join ira en medio de cada lista, tupla...

hora = "12:23"
print(hora.rpartition(":")) #Divide la cadena en 3 partes, la parte antes del caracter pasado por parámetro, el caracter y la parte después del caracter #Es como si fuera el split en java
print(hora.rpartition("/"))

print(hora.partition(":")) #Lo mismo pero empieza a buscar desde el principio #Si no encuentra el caracter pues la primera parte es la cadena entera y las otras dos vacías
print(hora.partition("/"))

hora = "12:23:12"
print(hora.partition(":")) #Esto es lo que pasa solo es el primero que encuentra

print(hora.split(":")) #Divide la cadena en una lista donde cada elemento es una parte de la cadena que estaba separada por el caracter pasado por parámetro 
#Esta opción permite aplicarlo a varios caracteres iguales y encima en lista que es más manejable

print(hora.rpartition(":")) #Esto es lo de antes el no mira el primero solo mira el último
print(hora.rsplit(":",2)) #Esto es como el split pero empieza a contar desde el final y el segundo parámetro es el número de divisiones que quieres hacer
#Si le digo 2 le fuerzo a que los 2 puntos no desaparezcan en la lista

texto = "Linea 1\nLinea 2\nLinea 3" 
print(texto.splitlines()) #Divide la cadena en una lista donde cada elemento es una parte de la cadena que estaba separada por los saltos de linea \n

##EJERCICIOS CADENAS:
# Crear un programa que lea por teclado una cadena y un carácter, e inserte el carácter entre cada letra de la cadena. 
# Ej: separar y , debería devolver s,e,p,a,r,a,r

# cadena = input("Introduce una cadena: ")
# caracter = input("Introduce un caracter: ")

# cadenaCambiada = caracter.join(cadena)

# print(cadenaCambiada)

# Crear un programa que lea por teclado una cadena y un carácter,
# y reemplace todos los dígitos en la cadena por el carácter. Ej: su clave es: 1540 y X debería devolver su clave es: XXXX

# cadena = input("Introduce una cadena: ")
# caracter = input("Introduce un caracter: ")
# cadena2 = cadena                                        #NO SE PORQUE NO FUNCIONA 
# for i in range(len(cadena)):
#     cadena2 = cadena.replace(str(i), caracter)

# print(cadena2)

# Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:

# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
# Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina debe devolver República Argentina.
# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.

# cadena = input("Introduce una cadena: ")

# cadenaPartida = cadena.split(" ")

# for palabra in cadenaPartida:
#     if palabra.startswith("a") or palabra.startswith("A"):
#         print(palabra, end=" ")
#     for primeraLetra in palabra[0]:
#         print(primeraLetra.capitalize(), end="")


# Escribir funciones que dadas dos cadenas de caracteres:

# Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, cadena es una subcadena de subcadena.
# Devuelva la que sea anterior en orden alfabético. Por ejemplo, si recibe kde y gnome debe devolver gnome.

# cadena1 = input("Introduce la primera cadena: ")
# cadena2 = input("Introduce la segunda cadena: ")

# if cadena2 in cadena1:
#     print("La segunda cadena es una subcadena de la primera")
# else:
#     print("La segunda cadena NO es subcadena de la primera")

# print(cadena1 if cadena1 < cadena2 else cadena2) #If ternario como en js

# Escribir un programa python que dado una palabra diga si es un palíndromo. Un palídromo Un palíndromo es una palabra, 
# número o frase que se lee igual hacia adelante que hacia atrás. Ejemplo: reconocer

# #Mi solución
# palabra = input("Escribe una palabra: ")
# invertir = list(palabra)
# invertir.reverse()

# print(invertir)
# print(palabra)

# if (list(palabra) == invertir):
#     print("Es un polindromo")
# else:
#     print("NO es un polindromo")

# #Solución web y más optima que la mía

# cad1=input("Cadena:")	
# if cad1.lower()==cad1[::-1].lower():
# 		print("palindromo")
# else:
# 		print("no palindromo")
            
#Bytes

#Se pueden definir de distintas maneras

byte1 = b"Hola"
#byte2 = b'¿Qué tal?' Con las comillas simple me salta error
byte3 = b'''Hola,que tal?''' #En definitiva poniendole la b antes

#podemos usar el constructor

byte1=bytes(10)
print(byte1) ##Secuencia con los numeros hexadecimales del rango

byte2=bytes(range(10)) 
print(byte2)

byte3=bytes.fromhex('2Ef0 F1f2') ##Con este metodo podemos pasar la cadena hexadecimal a un objeto de tipo bytes
print(byte3)

#Ahora pasamos con uno que si es MUTABLE y es Bytearray

ba1=bytearray() #No tiene nada
print(ba1)

ba2=bytearray(10) #Con 10 numeros hexadecimales
print(ba2)

ba3=bytearray(range(10))
print(ba3)

ba4=bytearray(b"hola")
print(ba4)                                  #En estos 2 se ha printeado como esta escrito
ba5=bytearray.fromhex('2Ef0 F1f2')
print(ba5)

#Propiedades igual que los demás de secuencia y también las funciones

#Demostración mutabnle e inmutable

#byte=b"hola" ##ERROR NO SE PUEDE HACER
#byte[2]=b'g'

ba1=bytearray(b'hola')
ba1[2]=123
print(ba1)
del ba1[3]
print(ba1)

#Los metodos de estos elementos en python son compatibles con muchas funciones que hemos visto los bytes son compatibles con los de cadena y los bytearray pues con
#los de listas

#Métodos encode y decode

#byte1=b'piña' #Da error porque no se puede representar en ASCII

byte1=bytes('piña',"utf-8")
print(byte1) #Pero codificando en utf 8 si podemos
print(len(byte1)) #Son 5 bytes ya que ñ ocupa 2

byte1=bytes('piña',"latin1")
print(byte1) #Probando otro codificador

#Podemos usar encode para convertir cadena unicode a bytes

cad="piña"
byte1=cad.encode("utf-8")
print(byte1)

#Al reves seria decode

print(byte1.decode("utf-8"))

#Pero no podemos usar decode y encode si son difrentes codificadores

byte1=bytes('piña',"latin1")
# byte1.decode("utf-8") #NO SE PUEDE

print(byte1.decode("utf-8","ignore")) #Está opcion ignora al caracter que no tiene

print(byte1.decode("utf-8","replace")) #Para que salga al menos con el simbolo cuando te falla la codificacion

##CONJUNTOS

#SET
#Guardar conjuntos desordenados de datos que se pude calcular una funcion hash que no hay repes. Es mutable

#Se usan para buscar, no hay duplicados y para cpalculos matematicos como interseccion, union, diferencia

#Definirlo de varias maneras

set1 = set()
print(set1)

set2=set([1,1,2,2,3,3])
print(set2)
set3={1,2,3} ##O con parentesis pero tienes que poner una lista o los corchetes
print(set3)

#Frozenset

#Este con diferencia al anteior es inmutable

fs1=frozenset()
print(fs1)
fs2=frozenset([1,1,2,2,3,3])
print(fs2)
#lo unico que se diferencia que en el print se muestran los parentesis con el {}

#Aqui cambia ta que los conjuntos solo sirven para recorrer y in, not in
#Las funciones igual que los demás de secuencia

set1={1,2,3}
set1.add(4)
print(set1) #LOS SET SON MUTABLES ASI QUE LOS FROZENSET NO TIENEN LOS METODOS
set1.remove(2)
print(set1)

#METODOS DE SET Y FROZENSET

set1={1,2,3}
set2={2,3,4}

print(set1.difference(set2)) #la diferencia entre set
print(set1.difference_update(set2)) #Este no devuelve nada cambia el set correspondiente con la diferencia que tiene



print(set1.symmetric_difference(set2)) #Esta vez cambia que devuelve los numeros diferentes entre ambos
print(set1.symmetric_difference_update(set2))

print(set1.intersection(set2)) #Los que son comunes entre los dos
print(set1.intersection_update(set2))

print(set1.union(set2)) #Hace una union quitando los repetidos
print(set1.update(set2))

#AÑADIR Y ELIMINAR ELEMENTOS

set1 = set()
set1.add(1)
set1.add(2)
print(set1)
set1.discard(3) #No da error si no hay
#set1.remove(3) #Si da error si lo hay
set1.pop()
print(set1)

#Metodos de comprobacion

set1 = {1,2,3}
set2 = {1,2,3,4}
print(set1.isdisjoint(set2))	##Tiene algo en común?
print(set1.issuperset(set2)) #Todos los elementos de set2 estan en set1 como si fuera un subconjunto
print(set2.issuperset(set1))

#frozenset tiene estos metodos en común con set pero modicado el nombre 

#ITERADOR Y GENERADOR

iter1 = iter([1,2,3])
print((type(iter1)))
iter2 = iter("hola")
print((type(iter2))) ##El tipo cambia pero sigue siendo un iterador pero string

#next sirve para recorrer paso a paso manualmente

print(next(iter1))
print(next(iter1))
print(next(iter1))

#Si hacemos un next mas dará error porque no hay mas elementos iterables

#reversed: invierte al iterador para que empieze por el final

iter2 = reversed([1,2,3])
print(next(iter2))
print(next(iter2))
print(next(iter2))
#Si hacemos un next mas dará error porque no hay mas elementos iterables

#El modulo itertools tiene cosas interesantes para los iterables

#Count devuelve un iterador infinito

from itertools import count
counter = count(start=13)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter)) #Las que queramos porque no hay limete

#Cycle devuelve una secuencia infinita

from itertools import cycle
colors = cycle(['red', 'white', 'blue'])
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
#Es como si fuera un bucle una serpiente que se muerde la cola

#islice devuelve un iterador infinito

from itertools import islice

limited = islice(colors, 0, 4) 
for x in limited: 
     print(x) 

#Generadores
#Es un tipo de iterador, obtener resultados paso a paso
#Esta yield pero lo veremos más adelante
#Pero podemos usar las listas comprimidas

iter1 = (x for x in range(10) if x % 2==0)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
#Como te pases del rango da error

#DICCIONARIOS
#Clave valor como en java

#Definición y construcción

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)

#COMO ES MUTABLE TAMBIEN PODEMOS HACERLO DE LA SIGUIENTE MANERA

dict1 = {}
dict1["one"]=1
dict1["two"]=2
dict1["three"]=3

#Operaciones basicas

#Ver numero de elementos clave valor
a = dict(one=1, two=2, three=3)
print(len(a))

#Indexion 

a["one"]
a["one"]+=1
print(a)

#Pero como indexemos uno que no existe da error

#Borrar con del 

del(a["one"])
print(a)

#tambien da error si no se encuentra

#pertenencia in not in

print("two" in a)

#iter devuelve un iterador pero de las claves

print(next(iter(a)))

#Son mutables por lo tanto....

a = dict(one=1, two=2, three=3)
a["one"]=2
del(a["three"])
print(a)

a = dict(one=1, two=2, three=3)
b = a
del(a["one"])
print(b) #Se borra porque esta copiando pero en direccion de memoria

#Para copiar diccionarios usamos el metodo copy (No pasa lo de antes)

a = dict(one=1, two=2, three=3)
b = a.copy()
a["one"]=1000
print(b)

#Con clear borrar diccionario entero

dict1 = dict(one=1, two=2, three=3)
dict1.clear()
print(dict1)

#Métodos de agregado y creación

#Copy
dict1 = dict(one=1, two=2, three=3)
dict2 = dict1.copy()
dict1["one"] = 1000
print(dict2) #No se modifica en la copia

#fromkeys
print(dict.fromkeys(["one","two","three"])) #Podemos crear dicionarios con valores a none
print(dict.fromkeys(["one","two","three"],100)) #Podemos crear todos con el mismo valor en este caso 100

#Update

dict1 = dict(one=1, two=2, three=3)
dict2 = {'four':4,'five':5}
dict1.update(dict2) 
print(dict1) #Podemos combinar 2 diccionarios con este metodo

#Setdefault

dict1 = dict(one=1, two=2, three=3)
dict1.setdefault("four", 4) ##Si no añadimos el segundo parametro el valor sera none
print(dict1) #Si no existe modifica nada y no devuelve nada

print(dict1.setdefault("two", 999)) ## Dice el valor del que intentamos modificar
print(dict1)

#Métodos de retorno 

#GET

dict1 = dict(one=1, two=2, three=3)
print(dict1.get("one")) #Obtenemos el valor
print(dict1.get("four")) #None si no existe
print(dict1.get("four", "no existe ;)")) #Pero podemos devolver algo con el segundo parametro

#POP

print(dict1.pop("one"))
print(dict1) ##Lo elimina del diccionario
##print(dict1.pop("four")) ##Pero como no exista peta
dict1.pop("four","no existe") ##Pero se puede prevenir con el segundo parametro

#POPITEM

dict1 = dict(one=1, two=2, three=3)
print(dict1.popitem()) ##Aleatorio la eliminación
print(dict1)


#Items

dict1 = dict(one=1, two=2, three=3)
print(dict1.items()) ##Me da todos sus elementos mostrados en cadena

#Keys


print(dict1.keys()) ##Me da todas las claves

#Tipo de datos dictviews

#Vista dinamica del diccionario

dict1 = dict(one=1, two=2, three=3)
i = dict1.items()
print(i)
dict1["four"]=4 #Lo que se ve es que al mostrar con itemns() pues los devuelve con este nuevo tipo de dato
print(i)

 #Funciones compatibles len, iter, x in dictview

#Recorrer diccionarios

for clave in dict1.keys():
    print(clave)            #Claves

for valor in dict1.values():
    print(valor)  #Valores

#O ambos

for clave,valor in dict1.items():
    print(clave,"->",valor)

#EJERCICIOS

# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. 
# Por ejemplo, si recibe “Qué lindo día que hace hoy” debe devolver: ‘que’: 2, ‘lindo’: 1, ‘día’: 1, ‘hace’: 1, ‘hoy’: 1


# diccionario = dict()

# cadena = input("Escribe una cadena: ").lower()

# listaPalabrasSep = cadena.split(" ")

# for palabra in listaPalabrasSep:
#     if palabra in diccionario.keys():
#         diccionario[palabra] += 1
#     else:
#         diccionario[palabra] = 1;

# print(diccionario)

# Tenemos guardado en un diccionario los códigos morse corespondientes a cada caracter. Escribir un programa que lea una palabra y 
# la muestre usando el código morse.

dic_morse = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
}

palabraUsuario = input("Escribe una palabra: ").upper()

textoEnMorse = ""
for letra in palabraUsuario:
   morse =  dic_morse.get(letra, "")
   textoEnMorse += morse + " "

print(textoEnMorse)

# Continuar el programa: ahora nos pide un código morse donde cada letra esta separada por espacios y nos da la cadena correspondiente.

dic_morse = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
}

morse = input("Morse: ") 
lista_morse_letra = morse.split(" ")
palabra = ""

for codigo in lista_morse_letra:
    letra = [key for key, valor in dic_morse.items() if valor == codigo][0] #Lista de compresion que tenemos un elemento que lo tenemos que seleccionar
    print(len(letra))
    palabra += letra

print(palabra)

# Suponga un diccionario que contiene como clave el nombre de una persona y como valor una lista con todas sus “gustos”. Desarrolle un programa que agregue “gustos” a la persona:

# Si la persona no existe la agregue al diccionario con una lista que contiene un solo elemento.
# Si la persona existe y el gusto existe en su lista, no tiene ningún efecto.
# Si la persona existe y el gusto no existe en su lista, agrega el gusto a la lista.
# Se deja de pedir personas cuando introducimos el carácter “*”.

gustos={}

nombre = input("Nombre:")
while nombre!="*":
	gusto=input("Gusto:")
	lista_gustos=gustos.setdefault(nombre,[gusto])
	if lista_gustos!=[gusto]:
		gustos[nombre].append(gusto)
	nombre = input("Nombre:")
print(gustos)