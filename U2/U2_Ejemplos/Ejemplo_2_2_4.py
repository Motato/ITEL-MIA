# Escriba un programa para verificar si un número es par o impar.

numero = int(input("Escriba un número entero: "))
if numero % 2 != 0:
    print(f"El número {numero} es impar.")
else:
    print(f"El número {numero} es par.")