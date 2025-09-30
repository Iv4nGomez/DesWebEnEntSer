# nombre = input("Introduce el nombre del videojuego: ")
# valoracion = input("Introduce la valoracion del videojuego: ")
# categoria = input("Introduce la categoria del videojuego: ")

# videojuego = {'nombre': nombre, 'valoracion': valoracion, 'categoria': categoria}

# print(videojuego)

videojuegos = []

nVideojuegos = int(input("Introduce el numero de videojuegos: "))

for i in range(nVideojuegos):
    nombre = input("Introduce el nombre del videojuego: ")
    valoracion = int(input("Introduce la valoracion del videojuego: "))
    categoria = input("Introduce la categoria del videojuego: ")
    videojuego = {'nombre': nombre, 'valoracion': valoracion, 'categoria': categoria}
    videojuegos.append(videojuego)

print(videojuegos)


for juego in videojuegos:
    print(juego["nombre"])
print("Media de todas las valoraciones: ", sum([juego["valoracion"] for juego in videojuegos])/len(videojuegos))

#Tarea:
#Crear lista en una sola linea con todos los nombres de los videojuegos

nombreJuegos = [juego.get("nombre") for juego in videojuegos]
print(nombreJuegos)

#Crear lista en una sola linea con todos las valoraciones de los videojuegos

valoracionesJuegos = [juego.get("valoracion") for juego in videojuegos]
print(valoracionesJuegos)

