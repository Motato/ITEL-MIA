"""
Diseña un programa que, dados dos números, muestre por pantalla uno de estos	
mensajes: «El segundo es el cuadrado del	primero.», «E1 segundo es menor que	el	
cuadrado del primero.» o bien «El segundo es mayor que el cuadrado del primero.»,	
dependiendo	de la verificación	de	la	condición correspondiente al significado de 
cada mensaje.
"""

import sys

# Mostrar codificación actual
print("Codificación por defecto:", sys.getdefaultencoding())

def comparar_cuadrado():
    while True:
        try:
            # Título con fallback si hay error de codificación
            try:
                print("\n🔍 Comparador de Cuadrado")
            except UnicodeEncodeError:
                print("\nComparador de Cuadrado")

            n1 = float(input("Ingrese el primer número: "))
            n2 = float(input("Ingrese el segundo número: "))

            cuadrado = n1 ** 2

            if n2 == cuadrado:
                try:
                    print("✅ El segundo es el cuadrado del primero.")
                except UnicodeEncodeError:
                    print("El segundo es el cuadrado del primero.")
            elif n2 < cuadrado:
                try:
                    print("📉 El segundo es menor que el cuadrado del primero.")
                except UnicodeEncodeError:
                    print("El segundo es menor que el cuadrado del primero.")
            else:
                try:
                    print("📈 El segundo es mayor que el cuadrado del primero.")
                except UnicodeEncodeError:
                    print("El segundo es mayor que el cuadrado del primero.")

        except ValueError:
            try:
                print("⚠️ Error: Por favor ingrese valores numéricos válidos.")
            except UnicodeEncodeError:
                print("Error: Por favor ingrese valores numéricos válidos.")

        # Preguntar si desea repetir
        repetir = input("\n¿Desea comparar otros números? (s/n): ").strip().lower()
        if repetir != 's':
            try:
                print("👋 Gracias por usar el comparador. ¡Hasta pronto!")
            except UnicodeEncodeError:
                print("Gracias por usar el comparador. ¡Hasta pronto!")
            break

# Ejecutar el programa
comparar_cuadrado()