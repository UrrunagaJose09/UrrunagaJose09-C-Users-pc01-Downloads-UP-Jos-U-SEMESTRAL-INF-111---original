def sumar_digit():
    print("------------------------------------------")
    print("| 34. Sumar dígitos de un número         |")
    print("------------------------------------------")
    
    numero = input("Ingrese un número entero: ")
    

    try:
        numero = int(numero)
    except ValueError:
        print("Error: Debes ingresar un número entero.")
        return
    
   
    numero = abs(numero)
    
   
    numero_str = str(numero)
    
    suma_digitos = 0
    
   
    for digito in numero_str:
        suma_digitos += int(digito)
    
    print(f"La suma de los dígitos de {numero} es: {suma_digitos}")