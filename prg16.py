def clasfic_edad():
    print("--------------------------------------------------------------")
    print ("/ 16. Clasificar la categoría de edad /")
    print("--------------------------------------------------------------")


    edad= float(input("Ingrese su edad: "))

    if edad >= 0 and edad <= 12:
        print("infantil")

    if edad >= 13 and edad <= 19:
        print("adolescente")

    if edad >= 20 and edad <= 59:
        print("adulto")

    if edad >= 60: 
        print("adulto mayor")