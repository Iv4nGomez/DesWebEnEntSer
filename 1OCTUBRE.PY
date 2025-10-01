asignatura1 = {"nombre":"servidor","profesor":"JI", "horas": 7}
asignatura2 = {"nombre":"cliente","profesor":"David", "horas": 6}

notas = {"cliente":9, "servidor":4}
persona = {"nombre":"David", "esProfe": True, "edad": 37, "asignaturas":[asignatura1,asignatura2], "notas":notas}

alumnos = []
alumnos.append(persona)
#Nota media 

# totalNota = 0

# for nota in persona["notas"].values():
#     totalNota += nota

# mediaNota = totalNota / len(persona["notas"][0].values())
# print(mediaNota)

# for a in alumnos:
#     x = (list(a["notas"].values()))
#     print(f"Media de todas las notas: {sum(x)/len(x)} ")


for a in alumnos:
    x = list(a[["notas"].values()])
    print(f"Media de {a['nombre']}  {sum(x/len(x))})"


 

#Suspensos nombre de las asignaturas

# for nota in persona["notas"]:
#     print(nota)

    


# persona2 = persona

# persona2["nombre"] = "Pablo"

# print(persona)
# print(persona2) #Direccion de memoria!!!

# alumnos = []
# alumnos.append(persona)
# print(alumnos[0]["asignaturas"][0]["horas"])

# # del(persona["esProfe"]) #Elimina tanto clave como valor
# # del(persona) #Borra el diccionario

# del(persona["esProfe"]) #
# print(persona.pop("nombre")) ##Devuelve lo que elimina

# for i in asignatura1.keys():
#     print(i)


# for i in asignatura1.values():
#     print(i)


# for c, v in asignatura1.items():
#     print("Clave:", c, "Valor", v)

# alumnos = []
# alumnos.append(persona)

