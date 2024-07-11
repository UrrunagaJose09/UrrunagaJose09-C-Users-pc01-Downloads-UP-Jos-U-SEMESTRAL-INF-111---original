def divs_3_5_deter():
    print("--------------------------------------------------------------")
    print ("/ 28. determinar si un número es divisible por 3 y 5 /")
    print("--------------------------------------------------------------")

    nmr = int(input("Introduce un número: "))


    if nmr % 3 == 0 and nmr % 5 == 0:
        print("El número es divisible por 3 y por 5.")

    if nmr % 3 == 0:
        print("El número es divisible por 3.")

    if  nmr % 5 == 0:
        print("El número es divisible por 5.")

    else:
        print("El número no es divisible ni por 3 ni por 5.")
