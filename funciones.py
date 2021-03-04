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
    lista = []
    for var in fich:
        if var.get("name") == buscar:
            return print (var.get("description"))