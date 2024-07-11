def cajer_simulator():
    print("------------------------------------------")
    print("/ 40. Simulador de cajero automatico  /")
    print("------------------------------------------")

    pin= 9009
    ints= 3

    while ints > 0:
        nmr= float(input("Ingrese su pin: "))

        while nmr == pin:
            print("Bienvenido a su cuenta")
            break

        else:
            ints -= 1

            if ints > 0:
                print(f"Te quedan {ints} intentos")

            else:
                print("Su cuenta se bloqueo")


