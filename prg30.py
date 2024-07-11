def tarif_tax():
    print("--------------------------------------------------------------")
    print ("/ 30. Calcula la tarifa de un taxi /")
    print("--------------------------------------------------------------")


    ki=float(input("ingrese el monte: "))

    if ki < 10:
        tarifa=ki * 2.50
    else:
        tarifa= 10 * 2.50 +( ki -10) *2.00
        print(f"La tarifa del taxi es de: {tarifa}")