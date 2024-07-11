def trian_verefic():
    print("--------------------------------------------------------------")
    print ("/ 24. Verificar si un triángulo es valido/")
    print("--------------------------------------------------------------")

    ld1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
    ld2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
    ld3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

    if ld1 + ld2 > ld3 or ld1 + ld3 > ld2 or ld2 + ld3 > ld1:
        print("Los lados ingresados forman un triángulo válido.")
    else:
        print("Los lados ingresados no forman un triángulo válido.")
