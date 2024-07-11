def licenc_deter():
    print("--------------------------------------------------------------")
    print ("/ 27. Determinar el tipo de licencia /")
    print("--------------------------------------------------------------")

    edad= float(input("Ingrese la edad: "))

    if edad >= 16 and edad <= 17:
        print("Licencia de menor")

    if edad >= 18 and edad < 65:
        print("Licencia de adulto")

    if edad >= 65:
        print("Licencia de mayor")