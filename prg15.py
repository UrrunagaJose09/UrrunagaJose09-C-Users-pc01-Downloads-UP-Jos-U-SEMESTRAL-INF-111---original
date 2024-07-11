def verif_5():
    print("--------------------------------------------------------------")
    print ("/ 15. Verificar si una palabra tiene mas de 5 letras /")
    print("--------------------------------------------------------------")


    plb = input("Ingrese una palabra: ")
    x= len(plb)

    if x >= 5:
        print(f"La palabra {plb} tiene 5 letras o mas")

    else:
        print("No tiene 5 palabras")

