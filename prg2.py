def impuesto_p():
    print("--------------------------------------------------------------")
    print ("/ 2. Impuesto de un producto /")
    print("--------------------------------------------------------------")

    
    pre= float (input("ingresar precio "))
    cant= float(input("ingresar cantidad "))

    ipt= float(input("ingresar cantidad de impuesto "))
    total=((pre*cant)*ipt)

    print(f"El total del impuesto del prodcuto es de: {total} ")   
    