"""
Realiza	un programa	que	calcule	el desglose	mínimo en billetes y monedas de	una	
cantidad exacta	de euros Hay billetes de 500, 200, 100,	50,	20,	10 y 5	€ y	monedas	
de 2 y l €. Por ejemplo, si deseamos conocer el desglose de 434 €, el programa	
mostrará por pantalla el siguiente resultado:	
2 billetes de 200 euros.	
1 billete de 20	euros.	
1 billete de 10 euros.    
2 monedas de 2 euros.
"""

import sys

def calcular_desglose(cantidad):
    denominaciones = [
        (500, "billete"),
        (200, "billete"),
        (100, "billete"),
        (50, "billete"),
        (20, "billete"),
        (10, "billete"),
        (5, "billete"),
        (2, "moneda"),
        (1, "moneda")
    ]
    desglose = []
    for valor, tipo in denominaciones:
        unidades = cantidad // valor
        if unidades:
            desglose.append((valor, tipo, unidades))
            cantidad %= valor
    return desglose

def mostrar_desglose(desglose, cantidad):
    try:
        print(f"\n🔍 Desglose de {cantidad} €:")
    except UnicodeEncodeError:
        print(f"\nDesglose de {cantidad} €:")
    for valor, tipo, unidades in desglose:
        palabra = tipo + ("s" if unidades > 1 else "")
        print(f"{unidades} {palabra} de {valor} euros.")

def main():
    print("Codificación por defecto:", sys.getdefaultencoding())
    while True:
        try:
            entrada = input("\nIngrese la cantidad exacta de euros (o escriba 'salir' para terminar): ").strip().lower()
            if entrada == "salir":
                try:
                    print("👋 Gracias por usar el desglose de euros. ¡Hasta pronto!")
                except UnicodeEncodeError:
                    print("Gracias por usar el desglose de euros. ¡Hasta pronto!")
                break

            cantidad = int(entrada)
            if cantidad < 0:
                print("⚠️ La cantidad debe ser positiva.")
            else:
                resultado = calcular_desglose(cantidad)
                mostrar_desglose(resultado, cantidad)

        except ValueError:
            print("⚠️ Error: Ingrese un número entero válido o 'salir' para terminar.")

# Ejecutar el programa
if __name__ == "__main__":
    main()

