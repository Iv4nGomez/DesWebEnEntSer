def suma(n, *agargs):
    resultado = n

    for i in agargs:
        resultado += i
    
    return resultado



print(suma(4, 5, 5, 20, 4))



def nombres(nombre="Ivan", **kwargs):
    cadena = "Alumnos: " + nombre
    for valor in kwargs.values():
        cadena = cadena + valor
    
    return cadena

print(nombres(nombre="Pepe", nombre2="Mario"))