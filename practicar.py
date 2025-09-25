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


##VERSIÓN OPTIMA
frase = input("Escribe una frase: ")
palabras = frase.split() #Split si no le ponemos ningún argumento pues todo los espacios, tabulaciones se iran fuera

print("Numeros de palabras: ", len(palabras))
print("La palabra mas larga es:", max(palabras, key=len) )##Cosa aprendida que me llevo key sirve para indicar como queremos ordenar los mayores (max) y los menores (min) es como si hicieramos el recorrido pero más simple
print("La palabra más corta es: ", min(palabras, key=len))
print("Palabras ordenadas alfabeticamente: ", sorted(palabras)) #Usar sorted para no cambiar el original para cambiarlo sort
      
      
      
      
      








