def salario_xh():
    print("--------------------------------------------------------------")
    print ("/ 6. Salario de un trabajo por hora  /")
    print("--------------------------------------------------------------")



    H=(float(input("ingresar horas por mes ")))
    P=(float(input("ingresar pago por hora ")))
    H_extra=(float(input("ingresar hora extra ")))
    st=(H*P)
    stx=((P*2)*H_extra)
    Total=(st+stx)

    print(f"El pago por hora durante un mes fue de {st} mas las horas extras qie hizo {Total}")