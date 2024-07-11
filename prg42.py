def sumar_numpares():
  print("------------------------------------------")
  print("/ 42. Sumar numeros pares del 1 al 100 / ")
  print("------------------------------------------")

  numeropar= 0 

  for i in range(1, 101):
    if i % 2 == 0:
      numeropar += i

  print(f"Los numero pares son: {numeropar}")