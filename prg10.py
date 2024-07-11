def conver_t():
    print("--------------------------------------------------------------")
    print ("/ 10. convertidor de temperatura /")
    print("--------------------------------------------------------------")


    c= float(input("ingresar celcius "))
    fht=((c*1.8)+32)
    klv=(c+273.15)

    print(f"La conversion de los celcius a farenheit es de {fht} y celsius a kelvin fue de {klv}")