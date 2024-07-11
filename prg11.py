def num_1x0():
    print("--------------------------------------------------------------")
    print ("/ 11. Verificar si el número es positivo, negativo o cero /")
    print("--------------------------------------------------------------")

    numero= float(input("Escriba un numero "))

    if numero > 0:
        print(f"El numero {numero} es positivo")

    if numero < 0:
        print(f"El numero {numero} es negativo")

    if numero == 0:
        print(f"El numero {numero} es el cero")


