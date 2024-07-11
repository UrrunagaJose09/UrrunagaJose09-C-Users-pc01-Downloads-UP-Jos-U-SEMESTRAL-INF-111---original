def draw_triang():
    print("------------------------------------------")
    print("/ 49. Dibujar un triangulo de asteriscos /")
    print("------------------------------------------")



    n = int(input("Ingrese un numero entero: "))
    for i in range(n+ 1):
        espacio = n - 1
        print("   " * espacio +  "*" * i  )