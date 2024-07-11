def des_p():
    print("--------------------------------------------------------------")
    print ("/ 9. Descuento de un producto /")
    print("--------------------------------------------------------------")


    P=(float(input("ingresa precio del producto ")))
    d=(float(input("ingresa descuento aplicado ")))
    i=(float(input("ingresa el impuesto del producto ")))
    Des=(P-(P*d))
    t_toal= ((Des*i)+ Des)

    print(f"El prodcuto tuvo un descuento de {Des} y el total a pagar es de {t_toal} ")
