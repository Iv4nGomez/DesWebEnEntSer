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

#JSON

def guardar_biblioteca(biblioteca, nombre_fichero):
  
        try: 
            with open(f"{nombre_fichero}.json", "w", encoding= "utf-8") as fichero:
                json.dump(biblioteca, fichero, indent=4, ensure_ascii=False) 
            print("Se ha guardado los datos correctamente!")
        except Exception:
            print(f"El fichero no se guardo correctamente")

def cargar_biblioteca(nombre_fichero):
    try:
        with open(f"{nombre_fichero}.json ", "r", encoding="utf-8") as fichero:
            datos = json.load(fichero)
        return datos
    except FileNotFoundError:
       print("No se encontro el fichero indicado, miralo bien anda")
       return []

def exportar_resumen(biblioteca, nombre_fichero):
    with open(f"{nombre_fichero}.txt", "w", encoding="utf-8") as fichero:
        for libro in biblioteca:
             for c, v in libro.items():
                 if (c == "prestamos"):
                     fichero.write(f"Préstamos totales: {sum(v.values())}\n")
                     break
                 fichero.write(f"{c}: {v} | ")

       




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

    #JSON

    if not cargar_biblioteca("biblioteca"):
          biblioteca = [
        {
            "titulo": "El principito",
            "autor": "Antonie de Saint-Exupéry",
            "anio": 1943,
            "genero": "Fábula",
            "prestamos": {"Manuel":5, "Antonio":3, "Fernando":3}
        },
        {
            "titulo": "Invisible",
            "autor": "Eloy moreno",
            "anio": 2020,
            "genero": "drama",
            "prestamos": {"Javier": 5, "Unay": 3, "Daniel": 4}
        },

        {
            "titulo": "Hábitos Atómicos",
            "autor": "Jeams Clear",
            "anio": 2020,
            "genero": "Desarrollo personal",
            "prestamos": {"Mariano": 5, "Pedro":5, "Carlos":4}
        },

         {
            "titulo": "Animales Fantasticos",
            "autor": "JK Rowling",
            "anio": 2015,
            "genero": "Misterio",
            "prestamos": {"Lucia": 5, "Laura":7, "Pepe":8}
        }

        

    ]
          
    guardar_biblioteca(biblioteca,"biblioteca")

    exportar_resumen(biblioteca, "resumen_biblioteca")


# Ejecutar programa
if __name__ == "__main__":
    main()
