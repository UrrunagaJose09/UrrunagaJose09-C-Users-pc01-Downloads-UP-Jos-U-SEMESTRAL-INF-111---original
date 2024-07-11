def num_deterprim():
    print("------------------------------------------")
    print("/ 47. Determinar si un numero es primo" ) 
    print("------------------------------------------")



    numero = int(input("Por favor, ingresa un número entero positivo: "))

    if numero <= 0:
        print("El número debe ser entero y positivo.")
    else:
        
        primo = True

        
        if numero < 2:
            primo = False
        else:
            
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    primo = False
                    break

    
        if primo:
            print("El número", numero, "es primo.")
        else:
            print("El número", numero, "no es primo.")

        
