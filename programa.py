from funciones import *
fich = leer_fichero("github/ejercicio_json/Campeoneslol.json")

opcion = menu()
while opcion != 6:
    if opcion == 1:
        for var in listar_campeones(fich):
            print (var)
        print()
    elif opcion == 2:
        for ca,ta in zip(listar_campeones(fich),contar_tag(fich)):
            if ta > 1:
                print (ca,"tiene",ta,"tags")
            else:
                print (ca,"tiene",ta,"tag")
        print ()
    elif opcion == 3:
        campe = input("De que campeón desea saber la descripción: ")
        mostrar_descrip(fich,campe.capitalize())
        print()

    opcion = menu()