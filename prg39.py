def binar_conver():
    print("------------------------------------------")
    print("/ 39. Convertir número a binario  /")
    print("------------------------------------------")

    ndc = int(input("Ingrese un número positivo: "))
    fnl= ""

    while ndc > 0:
        residuo = ndc % 2
        fnl = str(residuo) + fnl
        ndc = ndc // 2

        
        print(f"El número en binario es: {fnl}")