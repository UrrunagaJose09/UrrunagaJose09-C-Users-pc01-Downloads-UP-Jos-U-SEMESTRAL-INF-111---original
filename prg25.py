def trab_catg():
    print("--------------------------------------------------------------")
    print ("/ 25. Determinar la categoría de un trabajador /")
    print("--------------------------------------------------------------")

    Años=float(input("Ingrese los años de experiencia: "))

    if Años <= 2:
        print("Junior")

    if Años > 2 and Años <= 5:
        print("Semi-Senior")

    if Años > 5:
        print("Senior")