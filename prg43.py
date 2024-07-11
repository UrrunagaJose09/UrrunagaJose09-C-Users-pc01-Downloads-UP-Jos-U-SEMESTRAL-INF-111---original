def vocal_cont():
    print("------------------------------------------")
    print("/ 43. Contar vocales en una cadena /")
    print("------------------------------------------")


    x = input("ingresa una palabra o cadena: ")

    vocales = "aeiouAEIOU"


    contador= 0


    for caracter in x:

        if caracter in vocales:
            contador += 1

    print (f"La cadena tiene {contador} vocales")