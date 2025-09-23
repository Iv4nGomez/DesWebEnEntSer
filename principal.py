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