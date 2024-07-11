def cont_digit():
    print("------------------------------------------")
    print("/ 38. Contador de digitos /")
    print("------------------------------------------")


    numero = int(input("ingresa un número entero: "))
    digitos = 0


    if numero == 0:
        digitos = 1
    else:
        
        while numero > 0:
            
            numero = numero // 10
        
            digitos += 1


            print(f"El numero tiene {digitos} digitos ")
