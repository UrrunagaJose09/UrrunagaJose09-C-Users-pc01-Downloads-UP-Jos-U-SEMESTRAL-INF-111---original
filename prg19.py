def dtrg_l_d():
    print("--------------------------------------------------------------")
    print ("/ 19. Determinar si un carácter es una letra o digito/")
    print("--------------------------------------------------------------")

    X = input("Escribe un caracter ")

    if X.isdigit():
        print("Es un dígito")

    if X.isalpha():
        print("Es una letra")


