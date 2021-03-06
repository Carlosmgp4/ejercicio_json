import json
def leer_fichero(fichero):
    with open (fichero) as f:
        datos = json.load(f)
    return datos

def menu():
    print ("1. Mostrar nombre de todos los campeones")
    print ("2. Contar el número de tags de cada campeón")
    print ("3. Mostrar descripción de un campeón")
    print ("4. Mostrar que campeones pertenecen a un tag")
    print ("5. Mostrar campeón con la estadística mas elevada")
    print ("6. Salir del programa")
    opcion = int(input("Que acción le gustaría realizar: "))
    return opcion

def listar_campeones(fich):
    lista = []
    for cam in fich:
        campeon = cam.get("name")
        lista.append(campeon)
    return lista

def contar_tag(fich):
    lista = []
    for var in fich:
        tags = len(var.get("tags"))
        lista.append(tags)
    return lista

def mostrar_descrip(fich,buscar):
    for var in fich:
        if var.get("name") == buscar:
            return print (var.get("description"))

def lista_tag(fich):
    lista = []
    for var in fich:
        for t in var.get("tags"):
            if t not in lista:
                lista.append(t)
    return lista

def tag_campeones(fich,tag):
    lista = []
    for var in fich:
        if tag in var.get("tags"):
            lista.append(var.get("name"))
    return lista

def lista_estadis(fich):
    lista = []
    for var in fich:
        for e in var.get("stats").keys():
            if e not in lista:
                lista.append(e)
    return lista

def esta_maselevada(fich,nom):
    cont = -2
    for var in fich:
        if float(var.get("stats").get(nom)) > cont:
            cont = float(var.get("stats").get(nom))
            name = var.get("name")

    if cont == 0:
        return "No hay ningún personaje con puntuación en esta estadística."
    else:
        return name