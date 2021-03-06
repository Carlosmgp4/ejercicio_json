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
    elif opcion == 4:
        print ("Las tags disponibles para buscar son: ")
        for t in lista_tag(fich):
            print (t)
        print ()
        bus_ta = input("De que tag deseas saber el número de campeones que pertenecen a ella: ")
        print()
        print ("Los campeones con ese tag son: ")
        for d in tag_campeones(fich,bus_ta.capitalize()):
            print (d)
        print()
    elif opcion == 5:
        print ("Recuerda que el nombre de las estadisticas son: ")
        for var in lista_estadis(fich):
            print (var)
        print ()
        esta = input("Introduce el nombre de la estadistica, de la cual, quieres saber que campeón la tiene más elevada: ")
        print ("El campón con el",esta,"más elevado es: ",esta_maselevada(fich,esta))
        print()

    opcion = menu()