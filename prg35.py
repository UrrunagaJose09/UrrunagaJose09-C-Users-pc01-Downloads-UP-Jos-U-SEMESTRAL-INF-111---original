def adivi_num():
    print("------------------------------------------")
    print("/ 35. Adivinar un numero  /")
    print("------------------------------------------")

    import random


    nadiviar= random.randint(1,10)

    n= 0 

    while n != nadiviar:
        n= float(input("Adivina el numero entre 1 y 10: "))

        while n < nadiviar:
            print("El numero es mayor")
            break
            

        while n > nadiviar:
            print("El numero es menor")
            break
            
        

    print(f"Acertaste, el numero era: {nadiviar}")



