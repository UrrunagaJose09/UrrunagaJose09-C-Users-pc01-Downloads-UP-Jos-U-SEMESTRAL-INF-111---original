def sumar_limit():
    print("------------------------------------------")
    print("/ 33. Sumar numeros hasta un limite  /")
    print("------------------------------------------")

    limite = 100
    n = 0

    while n < limite:
        numero = float(input("Ingrese un numero: "))
        
        while numero <= 0:
            numero = float(input("Ingrese un numero: "))

        n = n + numero 
        print(f"La suma es: {n}")

    print(f"La suma final es: {n}")