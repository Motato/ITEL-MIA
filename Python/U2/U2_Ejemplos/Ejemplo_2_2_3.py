"""
Escriba un programa para verificar el usuario y contraseña de una persona. El
usuario deberá ser validado como "admin" y la contraseña "nazgull". 
"""
usuario = input("Ingresa el usuario: ")
contrasena = input("Ingresa la contraseña: ")
if usuario == "admin" and contrasena == "nazgull":
    print("El usuario y contraseña son válidos.")
else:
    print("El usuario o la contraseña no son válidos.")
    