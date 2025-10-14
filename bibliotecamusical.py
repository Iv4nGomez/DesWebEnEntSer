import json

#Funciones

def mostrarCanciones(canciones):
     for cancion in canciones:
          print([f'ID: {cancion["id"]} Titulo: {cancion["titulo"]} Artista: {cancion["artista"]} Año: {cancion["anio"]} Genero: {cancion["genero"]}'])
    
def añadirCancion(titulo, artista, anio, genero, canciones):
     for cancion in canciones:
          idNueva = cancion["id"] + 1
     cancionNueva = {"id":idNueva,"titulo":titulo, "artista":artista, "anio":anio, "genero":genero}
     canciones.append(cancionNueva)

def buscarPorTitulo(titulo, canciones):
     for cancion in canciones:
          if cancion["titulo"].lower() == titulo.lower():
            print(cancion)

def buscarPorArtista(artista, canciones):
     for cancion in canciones:
          if cancion["artista"].lower() == artista.lower():
            print(cancion)


def registrarUsuario(nombre, edad, pais, usuarios):
     nuevoUsuario = {"nombre_usuario":nombre, "edad":edad, "pais":pais, "favoritos":{}}
     usuarios.append(nuevoUsuario)
     
def añadirCancionFav(usuario, idcancion, valoracion, canciones, usuarios):
     existeCancion = False
     for cancion in canciones:
          if cancion["id"] == idcancion:
               existeCancion = True
     if existeCancion == False:
                print("La cancion que quieres añadir en favoritos no existe")
                return
     
     existeUsuario = False
     for usuario in usuarios:
          if usuario["nombre_usuario"] == usuario:
                existeUsuario = True
                usuario["favoritos"][idcancion] = valoracion
     
     if existeUsuario == False:
        print("El usuario no existe")
        return

def mostrarCancionesFav(usuario, usuarios, canciones):
     for usuario in usuarios:
          if usuario["nombre_usuario"] == usuario:
               for id, nota in usuario["favoritos"].items():
                    for cancion in canciones:
                         if cancion["id"] == id:
                              print(f"Titulo: {cancion["titulo"]} Valoracion: {nota}")

     
def filtrarCanciones(año, canciones):
     for cancion in canciones:
          if cancion["anio"] == año:
               print(cancion)


def estadisticas(usuarios, canciones):
    suma = 0
    contador = 0

    for usuario in usuarios:
        suma += sum(usuario["favoritos"].values())
        contador += len(usuario["favoritos"])

    if contador > 0:
        print("La media de las valoraciones es:", suma / contador)
    else:
        print("No hay valoraciones registradas.")



     

def main():
    try:
        with open("canciones.json", "r") as fichero:
            canciones = json.load(fichero)

    except FileNotFoundError:
            canciones = []    

    try:
        with open("usuarios.json", "r") as fichero:
            usuarios = json.load(fichero)

    except FileNotFoundError:
            usuarios = []  
    print("1. Mostrar todas las canciones","2. Añadir nueva canción","3. Buscar canciones por título o artista","4. Registrar nuevo usuario", "5. Añadir canción a favoritos de un usuario", "6. Mostrar canciones favoritas de un usuario","7. Filtrar canciones por género o año","8. Mostrar estadísticas (valoraciones y popularidad)","9. Guardar y salir", sep="\n")
    opcion = int(input("Introduce una opcion:"))
    while(not opcion == 9):
        if opcion == 1:
             mostrarCanciones(canciones)
        elif opcion == 2:
             titulo = input("Introduce un titulo para una cancion:")
             artista = input("Introduce el artista: ")
             anio = int(input("Introduce el año de publicacion:"))
             genero = input("Introduce el genero:")
             añadirCancion(titulo,artista,anio,genero, canciones)
        elif opcion == 3:
            usuarioEleccion = input("Quieres buscar la cancion por artista o titulo? (a/t)")
            if usuarioEleccion == "a":
                artista = input("Que artista quieres buscar:")
                buscarPorArtista(artista, canciones)
            else:
                titulo = input("Que titulo quieres buscar:")
                buscarPorTitulo(titulo, canciones)
        elif opcion == 4:
             nombre = input("Introduce el nombre:")
             edad = int(input("Introduce la edad: "))
             pais = input("Introduce el pais: ")
             registrarUsuario(nombre, edad, pais, usuarios)
        elif opcion == 5:
             usuario = input("Introduce el nombre del usuario:")
             idCancion = int(input("Introduce la ID de la cancion:"))
             valoracion = int(input("Introduce la valoracion de la cancion:"))
             añadirCancionFav(usuario, idCancion, valoracion, canciones, usuarios)

        elif opcion == 6:
             input("Introduce el nombre del usuario que quiere ver sus valoraciones:")
             mostrarCancionesFav(usuario, usuarios, canciones)
        elif opcion == 7:
             año = int(input("Año por el que quieres filtrar:"))
             filtrarCanciones(año, canciones)
        elif opcion == 8:
             estadisticas(usuarios, canciones)
  

        print("1. Mostrar todas las canciones","2. Añadir nueva canción","3. Buscar canciones por título o artista","4. Registrar nuevo usuario", "5. Añadir canción a favoritos de un usuario", "6. Mostrar canciones favoritas de un usuario","7. Filtrar canciones por género o año","8. Mostrar estadísticas (valoraciones y popularidad)","9. Guardar y salir", sep="\n")
        opcion = int(input("Introduce una opcion:"))
    
    with open("canciones.json", "w", encoding="utf-8") as fichero:
        json.dump(canciones, fichero, indent=4, ensure_ascii=False)
    with open("usuarios.json", "w", encoding="utf-8") as fichero:
        json.dump(usuarios, fichero, indent=4, ensure_ascii=False)
        print("DATOS GUARDADOS!")

if __name__ == "__main__":
    main()