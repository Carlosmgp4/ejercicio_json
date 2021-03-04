import json
def leer_fichero(fichero):
    with open (fichero) as f:
        datos = json.load(f)
    return datos

def listar_campeones(fich):
    lista = []
    for cam in fich:
        campeon = cam.get("name")
        lista.append(campeon)
    return lista