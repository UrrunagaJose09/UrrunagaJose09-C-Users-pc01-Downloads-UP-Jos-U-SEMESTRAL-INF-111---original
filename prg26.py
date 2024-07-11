def Imc_clas():
    print("--------------------------------------------------------------")
    print ("/ 26. Clasificar el IMC /")
    print("--------------------------------------------------------------")


    m = float(input("Ingrese su altura en metros: "))
    k = float(input("Ingrese su peso en kilogramos: "))


    Imc = k / (m ** 2)


    if Imc < 18.5:
        print(f"IMC: {Imc:.2f}")
        print("Bajo peso")

    elif 18.5 <= Imc < 24.9:
        print(f"IMC: {Imc:.2f}")
        print("Peso normal")

    elif 25 <= Imc < 29.9:
        print(f"IMC: {Imc:.2f}")
        print("Sobrepeso")

    elif Imc < 30.0: 
        print(f"IMC: {Imc:.2f}")
        print("Obesidad")
