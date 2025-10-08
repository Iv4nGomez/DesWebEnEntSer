import json

# -----------------------------
# Gestión de Biblioteca Digital
# -----------------------------

# Funciones

def mostrar_libros(biblioteca):
    # Recorre la lista y muestra la información de cada libro

    for libro in biblioteca:
        print(libro)



def buscar_por_autor(biblioteca, autor):
    # Devuelve una lista con los títulos de un autor dado
    
    titulosAutor = [libro["titulo"] for libro in biblioteca if libro["autor"] == autor]
    return titulosAutor

def prestamo(biblioteca, titulo, usuario):
    # Registra un préstamo de un libro por un usuario

    for libro in biblioteca:
        if titulo == libro["titulo"]:
            for usuarios in libro["prestamos"].keys():
                if usuarios == usuario:
                    libro["prestamos"][usuario] += 1
                    return biblioteca
                else:
                    libro["prestamos"][usuario] = 1
                    return biblioteca
              
    return "No se encontro el libro"
                
                


            


def libro_mas_popular(biblioteca):
    # Devuelve el libro con más préstamos totales
        libroMaxPrest = 0
        nombreLibro = None
        for libro in biblioteca:
            numPrestamosAct = sum(libro["prestamos"].values())
            if numPrestamosAct > libroMaxPrest:
                libroMaxPrest = numPrestamosAct
                nombreLibro = libro["titulo"]
        return nombreLibro
  

    
 

def estadisticas_usuarios(biblioteca):
    # Devuelve un diccionario con total de préstamos por usuario
    statsPrestamosUsr = {}

    for libro in biblioteca:
        for usuario, cantidad in libro["prestamos"].items():
            if usuario in statsPrestamosUsr:
                statsPrestamosUsr[usuario] += cantidad
            else:
                statsPrestamosUsr[usuario] = cantidad
    
    return statsPrestamosUsr


def guardar_biblioteca(biblioteca, nombre_fichero):
    with open(f"{nombre_fichero}.json" ) as fichero:
        json.dump(biblioteca, fichero)




# Programa principal
def main():
    # 1. Crear biblioteca con al menos 5 libros
    biblioteca = [
        {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "anio": 1967,
            "genero": "Novela",
            "prestamos": {"Gabriela":1, "Carlos":3, "Ivan":10}
        },
        {
            "titulo": "El Quijote",
            "autor": "Miguel de Cervantes",
            "anio": 1605,
            "genero": "Novela",
            "prestamos": {"Ismael": 5, "Marcos": 3, "Manuel": 4}
        },
        # Añadir más libros aquí...

        {
            "titulo": "Hábitos Atómicos",
            "autor": "Jeams Clear",
            "anio": 2020,
            "genero": "Desarrollo personal",
            "prestamos": {"Ivan": 1, "Blas":2, "Ruben":3}
        },

         {
            "titulo": "Harry Potter",
            "autor": "JK Rowling",
            "anio": 2005,
            "genero": "Misterio",
            "prestamos": {"Lucia": 5, "Javi":3, "Ruben":4}
        }

        

    ]

    # 2. Mostrar todos los libros

    mostrar_libros(biblioteca)

    # 3. Buscar por autor (pedir al usuario un nombre)

    nombreAutor = input("Introduce el nombre del autor: ")
    titulos = buscar_por_autor(biblioteca,nombreAutor)
    print(titulos)
    

    # 4. Simular préstamos

    tituloLibro= "Hábitos Atómicos"
    user = "Ana"

    bibliotecaModificada = prestamo(biblioteca, tituloLibro, user)

    for libro in bibliotecaModificada:
        if libro["titulo"] == tituloLibro:
            print(libro)

    
 
    
            
    # 5. Mostrar el libro más popular

    print("El libro más vendido es: ", libro_mas_popular(biblioteca))
   
   
    # 6. Mostrar estadísticas de usuarios

    diccionarioDevuelto = estadisticas_usuarios(biblioteca)

    for clave, valor in diccionarioDevuelto.items():
        print(f"{clave} -----> {valor}")

    
    guardar_biblioteca(biblioteca, "datos")

# Ejecutar programa
if __name__ == "__main__":
    main()
