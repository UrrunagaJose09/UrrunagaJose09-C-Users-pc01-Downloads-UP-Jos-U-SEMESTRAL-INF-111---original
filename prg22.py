def net_salar():
    print("--------------------------------------------------------------")
    print ("/ 22. Calcular el salario neto/")
    print("--------------------------------------------------------------")

    Sl= float(input("Ingrese su salario bruto: "))

    if  Sl >= 2000: 
        ipst= Sl*0.2
        SBruto= (ipst - Sl)
        print(f"El salario Neto es de:  {SBruto}")