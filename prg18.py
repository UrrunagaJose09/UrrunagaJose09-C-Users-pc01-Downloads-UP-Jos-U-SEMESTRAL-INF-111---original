def verif_rang():   
    print("--------------------------------------------------------------")
    print ("/ 18. Verificar si un número está en un rango /")
    print("--------------------------------------------------------------")


    num= float(input("Escribe un numero "))

    if num >= 1 and num <= 100:
        print(f"El numero {num} esta en rengo")

    else:
        print("No esta en el rango")
