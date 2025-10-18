def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error: División por cero"

def calculadora():
    print(" Calculadora Simple en Python")

    while True:
        try:
            n1 = float(input("Ingrese el primer número: "))
            n2 = float(input("Ingrese el segundo número: "))
            operacion = input("Ingrese la operación (+, -, *, /): ")

            operaciones = {
                '+': suma,
                '-': resta,
                '*': multiplicacion,
                '/': division
            }

            if operacion in operaciones:
                resultado = operaciones[operacion](n1, n2)
                print("Resultado:", resultado)
            else:
                print(" Operación no válida")

        except ValueError:
            print(" Error: Entrada no numérica")

        repetir = input("¿Desea realizar otra operación? (s/n): ").lower()
        if repetir != 's':
            print("Gracias por usar la calculadora. ¡Hasta pronto!")
            break

# Ejecutar la calculadora
calculadora()