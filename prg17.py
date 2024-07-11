def cal_des_if():
    print("--------------------------------------------------------------")
    print ("/ 17. Calcular el precio  con descuento /")
    print("--------------------------------------------------------------")


    prd= float(input("Ingrese el precio del producto "))

    if prd >= 100:
        descuento= prd * 0.10 
        des_total= prd - descuento
        print(f"El precio final del producto con el descuento es de: {des_total} ")