
# nombre = input("Introduce el nombre del videojuego: ")
# valoracion = input("Introduce la valoracion del videojuego: ")
# categoria = input("Introduce la categoria del videojuego: ")

# videojuego = {'nombre': nombre, 'valoracion': valoracion, 'categoria': categoria}

# print(videojuego)

videojuegos = []

nVideojuegos = int(input("Introduce el numero de videojuegos: "))

for i in range(nVideojuegos):
    nombre = input("Introduce el nombre del videojuego: ")
    valoracion = input("Introduce la valoracion del videojuego: ")
    categoria = input("Introduce la categoria del videojuego: ")
    videojuego = {'nombre': nombre, 'valoracion': valoracion, 'categoria': categoria}
    videojuegos.append(videojuego)

print(videojuegos)


for juego in videojuegos:
    print(juego["nombre"])
    print("Media de todas las valoraciones: ", sum(juego["valoracion"] / len(videojuegos)))

    



