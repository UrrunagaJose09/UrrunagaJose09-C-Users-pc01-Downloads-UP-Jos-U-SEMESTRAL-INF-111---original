def multip_num():
    print("------------------------------------------")
    print("/ 36. Mostrar multiplos de un numero /")
    print("------------------------------------------")


    numero=int(input("Ingrese numero: "))
    x=0
    for i in range(numero):
        if numero>0:
            x=x + i
            print(f"{x}")