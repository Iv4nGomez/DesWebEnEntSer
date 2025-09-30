videojuegos = ["Mario Kart World", "Spiderman 2", "The last of us 2", "God of war Ragnarok", "Fortnite"]
notas = []

for videojuego in videojuegos:
    nota  = int(input(F"Introduce la nota de este videjuego (1-10) {videojuego}: "))
    while nota > 10 or nota< 0:
        print("Has puesto una nota invalida: ")
        nota  = int(input(F"Introduce la nota de este videjuego (1-10) {videojuego}: "))
        break
    notas.append(nota)

for i in range(len(videojuegos)):
    print("Notas videojuegos: ")
    print(videojuegos[i], notas[i], sep= "...>")

print("Media de todoas las notas: ", sum(notas)/len(videojuegos)) 


videojuegosMasDeOcho = [videojuegos[i] for i in range(0,len(videojuegos)-1) if notas[i] >= 8]
print("Videojuegos con mas de un 8: " ,videojuegosMasDeOcho)

# notaMejor = max(notas)
# peorNota = min(notas)

# print("Videojuego más valorado; ", notaMejor)
# print("Videojuego menos valorado; ", peorNota)


listaMejorPeorNota = []


