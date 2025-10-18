""" Crear un programa con funciones para calcular el área de un triángulo, rectángulo, círculo, cubo y rombo. """

import math

# Funciones de área
def area_triangulo(base, altura): return (base * altura) / 2
def area_rectangulo(base, altura): return base * altura
def area_circulo(radio): return math.pi * radio ** 2
def area_cubo(arista): return 6 * arista ** 2
def area_rombo(D, d): return (D * d) / 2

# Diccionario de figuras
figuras = {
    '1': ('Triángulo', lambda: area_triangulo(float(input("Base: ")), float(input("Altura: ")))),
    '2': ('Rectángulo', lambda: area_rectangulo(float(input("Base: ")), float(input("Altura: ")))),
    '3': ('Círculo', lambda: area_circulo(float(input("Radio: ")))),
    '4': ('Cubo', lambda: area_cubo(float(input("Arista: ")))),
    '5': ('Rombo', lambda: area_rombo(float(input("Diagonal mayor: ")), float(input("Diagonal menor: "))))
}

def mostrar_menu():
    print("\nSeleccione la figura para calcular el área:")
    for clave, (nombre, _) in figuras.items():
        print(f"{clave}. {nombre}")
    print("6. Salir")

def main():
    print("Calculadora de Áreas")
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == '6':
            print("Gracias por usar la calculadora de áreas. ¡Hasta pronto!")
            break
        try:
            resultado = figuras[opcion][1]()
            print(f"Área del {figuras[opcion][0]}: {resultado:.2f}")
        except ValueError:
            print("Entrada inválida. Intente con números.")
        except KeyError:
            print("Opción no válida. Por favor, intente de nuevo.")

main()# Calculadora de áreas de figuras geométricas
