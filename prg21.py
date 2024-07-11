def num_prim():
    print("--------------------------------------------------------------")
    print ("/ 21. Determinar si es número primo /")
    print("--------------------------------------------------------------")

    numero= float(input("Ingrese el número "))

    a= 1
    b= 0

    while a <= numero:
        if numero % a == 0:
            b = b + 1
            a = a + 1

        if  a == 2:
            print(f"El número {numero} es primo")

        else:
            print(f"El número {numero} no es primo")