def sumar_numnatural():
        print("------------------------------------------")
        print("/ 46. Sumar los primeros N numeros naturales /")
        print("------------------------------------------")


        N = int(input("Por favor, ingresa un número entero positivo: "))
                
        suma= 0

        for i in range(1, N + 1):
                suma += i
                print(f"La suma de los primeros numero N naturales son {suma}")
