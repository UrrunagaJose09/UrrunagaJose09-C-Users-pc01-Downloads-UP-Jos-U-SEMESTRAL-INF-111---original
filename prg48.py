def cel_and_fhtr_conver():
    print("------------------------------------------")
    print("/ 48. Convertir grados a celsius a fahrenheit /")
    print("------------------------------------------")

    def X (celsius):
        return (celsius * 9/5) + 32


    inicio = int(input("Introduce la temperatura de inicio en grados Celsius: "))
    fin = int(input("Introduce la temperatura de fin en grados Celsius: "))


    print("Conversión de Celsius a Fahrenheit:")
    for celsius in range(inicio, fin + 1):
        fahrenheit = X (celsius)
        print(f"{celsius}°C = {fahrenheit:.2f}°F")

