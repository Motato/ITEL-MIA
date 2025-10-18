"""
Escriba un programa para verificar si una persona es mayor de edad, la
condición para que sea mayor de edad, es que la persona tenga 18 años o más, en caso de
que la persona tenga entre 0 y 17 años, la persona es menor de edad, en caso distinto la
persona no ha nacido
"""

edad = int(input("¿Cuántos años tienes? "))
if edad < 0:
    print(f"La persona aún no ha nacido, y su edad es de: {edad} años")
elif edad >= 0 and edad < 18:
    print(f"Usted es menor de edad, y su edad es: {edad} años")
else:
    print(f"Usted es mayor de edad, y su edad es: {edad} años")

