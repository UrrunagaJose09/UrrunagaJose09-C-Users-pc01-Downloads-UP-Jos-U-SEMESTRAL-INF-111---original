def valid_Ent():
    print("------------------------------------------")
    print("/ 37. validar  entrada  /")
    print("------------------------------------------")

    numero= float(input("Ingrese un numero positivo: "))

    while numero < 0:
        numero= float(input("No es positivo, ingrese un numero positivo: "))

        while numero > 0: 
            print(f"El numero {numero} es positivo")
            break