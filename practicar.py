# Ejercicio 1 – Básico
# Objetivo: Practicar listas y cadenas.

# Pide al usuario que introduzca una frase.
# Convierte la frase en una lista de palabras.
# Muestra por pantalla:
# Número de palabras.
# La palabra más larga.
# La palabra más corta.
# La lista de palabras ordenadas alfabéticamente.


#VERSION FUNCIONAL PERO NO OPTIMA
# frase = input("Escribe una frase: ")
# fraseDivPalabras = frase.split(" ")

# print(fraseDivPalabras)
                                                                    #Mal el bucle se reutiliza para los dos
# palabraMasGrande = ""                                             #La tecnica de palabra corta no es adecuada
# for palabra in fraseDivPalabras:
#     if(len(palabra) > len(palabraMasGrande)):
#         palabraMasGrande = palabra;
# print(palabraMasGrande)

# palabraMasCorta = "cortooooooooooooooooooooooooo"

# for palabra in fraseDivPalabras:
#     if(len(palabra) < len(palabraMasCorta)):
#         palabraMasCorta = palabra;
# print(palabraMasCorta)


# ##VERSIÓN OPTIMA
# frase = input("Escribe una frase: ")
# palabras = frase.split() #Split si no le ponemos ningún argumento pues todo los espacios, tabulaciones se iran fuera

# print("Numeros de palabras: ", len(palabras))
# print("La palabra mas larga es:", max(palabras, key=len) )##Cosa aprendida que me llevo key sirve para indicar como queremos ordenar los mayores (max) y los menores (min) es como si hicieramos el recorrido pero más simple
# print("La palabra más corta es: ", min(palabras, key=len))
# print("Palabras ordenadas alfabeticamente: ", sorted(palabras)) #Usar sorted para no cambiar el original para cambiarlo sort
      
# Ejercicio 2 – Contar vocales y filtrar palabras

# Pide al usuario que introduzca varias palabras separadas por espacios.
# Crea una lista con esas p alabras usando split().
# Filtra las palabras que tengan más de 3 vocales.
# Para contar vocales, puedes usar el truco que ya sabes:
# sum(1 for c in palabra.lower() if c in "aeiou")
# Muestra por pantalla la lista resultante.

##Version no optima
# palabras = input("Introduce varias palabras separadas por un espacio: ")
# lista = palabras.split()
# filtroTresVocales = ""

# for palabra in lista:
#     contadorVocales = 0
#     for letra in palabra:
#         if (letra.lower() in "aeiou"):
#             contadorVocales += 1
#     if (contadorVocales  > 3 ):
#         filtroTresVocales += palabra, " " ##Aqui error esto no se hace

# print(filtroTresVocales)

# # # palabras = input("Introduce distintas palabras separadas por espacio: ")
# # # lista = palabras.split()

# # # palabrasFiltradas = [palabra for palabra in lista if(sum(1 for letra in palabra if letra in "aeiou")) > 3] ##Mejora importante usar listas comprimidas ya que gemeras listas faciles sin tener que poner un bucle entero ni un if todo en una misma linea
    
# # # print(palabrasFiltradas)


# Ejercicio 3 – Palabras espejo y filtrado

# Pide al usuario que introduzca una frase.
# Separa la frase en palabras con split().
# Crea una nueva lista con palabras que sean palíndromos (se leen igual al derecho y al revés, por ejemplo: "ana", "oso").
# Además, de esa lista de palíndromos, selecciona solo las que tengan más de 3 letras.
# Muestra por pantalla la lista resultante.

# frase = input("Introduce una frase: ")
# palabras = frase.split()
 
# listaFiltrada = [palabra for palabra in palabras if palabra[::-1] == palabra and len(palabra) > 3 ] ##La lista comprimida una vez pillado el truco es lo mejor
      
# print(listaFiltrada)
      

# Ejercicio 4 – Desafío completo

# Objetivo: analizar una frase y generar estadísticas avanzadas de palabras.
# Pide al usuario que introduzca una frase.
# Separa la frase en palabras con split().
# Genera una lista de palabras únicas (sin repetir).
# Filtra solo las palabras que tengan más de 4 letras.
# Para cada palabra de la lista filtrada, calcula cuántas vocales tiene.
# Ordena la lista final de mayor a menor número de vocales.


##Como no se hace
# frase = input("Introduce una frase: ")
# palabras = frase.split()

# palabrasSinRepetir = [palabra for palabra in palabras if palabras.count(palabra) < 2  and len(palabra)>4  ]
# print(palabrasSinRepetir)
# palabrasVocales = [len(palabra) for palabra in palabrasSinRepetir]
# print(palabrasVocales)

# listaFinal = []
# for palabras, vocales in zip(palabrasSinRepetir, palabrasVocales):
#     listaFinal.append(palabras)
#     listaFinal.append(vocales)

# print(listaFinal)

##CORRECCION OTIMIZADA

#SET es la clave ya que este conjunto no se repite entonces nos lo quitamos directmanete
#Me he confundido y no he puesto el filtro de las vocales bien lo hecho por caracteres
#Mejor usar diccionarios o tuplas para esto
#Podemos usar en key una funcion anonima llamada lambax que podemos escoger como en la indexion el elemento de la tupla

##Ahora lo hago de nuevo optimizando estos puntos que he hecho mal 

# frase = input("Introduce una frase: ")
# palabras = frase.split()
# listaSinRepetir = [palabra for palabra in set(palabras) if(sum(1 for letra in palabra if letra in "aeiou")>4)]

# palabrasVocales = [(palabra , sum(1 for letra in palabra if letra in "aeiou")) for palabra in listaSinRepetir]

# ordenarPorVocales = sorted(palabrasVocales, key=lambda x: x[1], reverse=True)

# print(ordenarPorVocales)

# Ejercicio 1: Contar palabras únicas

# Pide al usuario una frase y muestra cuántas palabras distintas tiene.

#Como lo haria yo
# frase = input("Introduce una frase: ")
# palabras = frase.split()

# print("Tiene:" , len(set(palabras)), "palabras diferentes.")

# frase = input("Introduce una frase: ")
# palabras = frase.lower().split() #Lower para todo a minusculas

# print("Tiene:" , len(set(palabras)), "palabras diferentes.") #Los no alfanumericos se pueden solucionar con expresiones regulares pero eso ya lo vere mas adelante

#Optimizado con errores arreglado y lo más corto posible

# print("Tiene: ", len(set(input("Introduce una frase: ").lower().split())), "palabras distintas.") #Es una forma más optima PERO da igual en este caso el rendimiento va a ser el mismo


# Enunciado

# Crea una lista con los números del 1 al 20.
# Usa filter + lambda para quedarte solo con los números pares.
# Muestra el resultado.

listaNumeros = list(range(0,21))
listaFiltrada = list(filter(lambda n: n % 2 == 0, listaNumeros)) ##Filter si es tru devuelve un iterador que lo convertimos en lista

print(listaFiltrada)

# 🔹 Enunciado

# Pide al usuario una frase o una lista de palabras separadas por comas.
# Convierte la entrada en una lista de palabras.
# Ordénalas de menor a mayor longitud usando sorted con lambda como clave (key).
# Muestra la lista ordenada.

#SE PUEDE OTIMIZAR UN POCO MAS

# frase = input("Introduce varias palabras separadas por ,: ") ##CON STRIP PODEMOS OPTIMIZAR ESTO, PARA QUE LOS ESPACIOS NO IMPORTEN

# palabras = frase.split(", ")

# palabrasOrdenadas = sorted(palabras, key=lambda p: len(p))
# print(palabrasOrdenadas)

#OPTIMO
frase = input("Introduce varias palabras separadas por ,: ")
palabras = frase.strip().split(", ") #Quita los espacios que pueda poner el usuario


