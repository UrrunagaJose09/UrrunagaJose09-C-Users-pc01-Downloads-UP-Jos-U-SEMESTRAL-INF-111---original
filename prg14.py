def deter_v():
    print("--------------------------------------------------------------")
    print ("/ 14. Determinar si un carácter es una vocal /")
    print("--------------------------------------------------------------")


    x = input("Ingrese una letra: ").lower()


    if x in 'aeiou':
        print("Es una vocal")

    else:
        print("No es una vocal")