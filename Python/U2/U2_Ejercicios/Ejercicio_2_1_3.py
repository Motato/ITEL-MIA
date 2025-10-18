"""
Crea una función llamada es_palindromo(palabra) que determine si una palabra
es palíndroma (se lee igual de izquierda a derecha que de derecha a izquierda).
La función debe devolver True o False.

Después, implementa otra función llamada
filtrar_palindromos(lista_palabras) que reciba una lista de palabras y
devuelva solo aquellas que sean palíndromos.
"""

import unicodedata

def normalizar(palabra):
    palabra = palabra.lower().replace(" ", "")
    return ''.join(c for c in unicodedata.normalize('NFD', palabra) if unicodedata.category(c) != 'Mn')

def es_palindromo(palabra):
    palabra = normalizar(palabra)
    return palabra == palabra[::-1]

def filtrar_palindromos(lista_palabras):
    return [p for p in lista_palabras if es_palindromo(p)]

def main():
    print(" Filtro de Palíndromos")
    while True:
        entrada = input("Ingrese palabras separadas por comas: ")
        lista = [p.strip() for p in entrada.split(",") if p.strip()]
        if not lista:
            print(" No se ingresaron palabras válidas.")
            continue

        resultado = filtrar_palindromos(lista)
        print("\n Palíndromos encontrados:")
        if resultado:
            for palabra in resultado:
                print(f"– {palabra}")
        else:
            print("No se encontraron palíndromos.")

        if input("¿Desea ingresar otra lista? (s/n): ").lower() != 's':
            print("Gracias por usar el filtro. ¡Hasta pronto!")
            break

main()
