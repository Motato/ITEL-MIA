"""
Escriba un programa de adivinanzas, en donde el programa debe
adivinar el número pensado por el usuario.
"""
print("Piense en un número entre 1 y 4.")
print("Conteste S (si) o N (no) a las preguntas.")
primera = input("¿El número pensado es mayor que 2? ")
if primera == "S":
    segunda = input("¿El número pensado es mayor que 3? ")
    if segunda == "S":
        print("El número pensado es 4.")
    else:
        print("El número pensado es 3.")
else:
    segunda = input("¿El número pensado es menor que 2? ")
    if segunda == "S":
        print("El número pensado es 1.")
    else:
        print("El número pensado es 2.")
print("Gracias por jugar.")

