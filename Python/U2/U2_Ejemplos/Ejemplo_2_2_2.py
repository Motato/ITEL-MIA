"""
Escriba un programa para verificar si una persona es mayor de edad, la 
condición para que sea mayor de edad, es que la persona tenga 18 años o más, en caso 
contrario la persona es menor de edad.
"""
edad = int(input("Teclear la edad de la persona: "))
if edad >= 18:
    print(f"La persona tiene {edad} años, y es considerado un adulto.")
else:
    print(f"La persona tiene {edad} años, y es considerado un menor de edad.")


