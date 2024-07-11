def imprimr_impares():
   print("------------------------------------------")
   print("/ 45. Imprimir numero impares  /")
   print("------------------------------------------")


   n = int(input("ingresa un número entero positivo: "))

   for i in range(1, n + 1):
      if i % 2 != 0:
         print(i)

