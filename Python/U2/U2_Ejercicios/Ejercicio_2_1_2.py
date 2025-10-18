"""
Diseña una función llamada convertir temperatura (valor, escala) que reciba un
valor numérico y una escala de conversión ("C" para Celsius, "F" para Fahrenheit o
"K" para Kelvin).
"""

# Diccionarios de conversión
TO_CELSIUS = {
    'C': lambda x: x,
    'F': lambda x: (x - 32) * 5/9,
    'K': lambda x: x - 273.15
}

FROM_CELSIUS = {
    'C': lambda x: x,
    'F': lambda x: (x * 9/5) + 32,
    'K': lambda x: x + 273.15
}

def convertir_temperatura(valor, origen, destino):
    """
    Convierte un valor de temperatura entre Celsius, Fahrenheit y Kelvin.
    """
    if not isinstance(valor, (int, float)):
        return "El valor debe ser numérico."

    origen = origen.strip().upper()
    destino = destino.strip().upper()

    if origen not in TO_CELSIUS or destino not in FROM_CELSIUS:
        return "Escalas no válidas. Usa 'C', 'F' o 'K'."

    try:
        temp_c = TO_CELSIUS[origen](valor)
        return FROM_CELSIUS[destino](temp_c)
    except Exception as e:
        return f"Error inesperado: {e}"

# 🧑‍💻 Interfaz interactiva
def main():
    print("Conversor de Temperaturas (C, F, K)")
    while True:
        try:
            valor = float(input("Ingrese el valor de temperatura: "))
            origen = input("Ingrese la escala de origen (C, F, K): ")
            destino = input("Ingrese la escala de destino (C, F, K): ")

            resultado = convertir_temperatura(valor, origen, destino)
            print(f"Resultado: {valor}°{origen.upper()} = {resultado:.2f}°{destino.upper()}" if isinstance(resultado, (int, float, float)) else resultado)

        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

        continuar = input("¿Desea convertir otra temperatura? (s/n): ").lower()
        if continuar != 's':
            print("Gracias por usar el conversor. ¡Hasta pronto!")
            break

main()
