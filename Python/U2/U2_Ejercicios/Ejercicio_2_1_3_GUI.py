"""
Crea una función llamada es_palindromo(palabra) que determine si una palabra
es palíndroma (se lee igual de izquierda a derecha que de derecha a izquierda).
La función debe devolver True o False.

Después, implementa otra función llamada
filtrar_palindromos(lista_palabras) que reciba una lista de palabras y
devuelva solo aquellas que sean palíndromos.
"""


import tkinter as tk
from tkinter import ttk
import unicodedata

# ------------------ Lógica de palíndromos ------------------

def normalizar(palabra):
    palabra = palabra.lower().replace(" ", "")
    return ''.join(c for c in unicodedata.normalize('NFD', palabra) if unicodedata.category(c) != 'Mn')

def es_palindromo(palabra):
    palabra = normalizar(palabra)
    return palabra == palabra[::-1]

def filtrar_palindromos(lista_palabras):
    return [p for p in lista_palabras if es_palindromo(p)]

# ------------------ Función para la GUI ------------------

def detectar_palindromos():
    entrada = entry_palabras.get()
    lista = [p.strip() for p in entrada.split(",") if p.strip()]
    
    if not lista:
        resultado_text.set("⚠️ No se ingresaron palabras válidas.")
        return

    resultado = filtrar_palindromos(lista)
    if resultado:
        resultado_text.set("✅ Palíndromos encontrados:\n" + "\n".join(f"– {p}" for p in resultado))
    else:
        resultado_text.set("❌ No se encontraron palíndromos.")

# ------------------ Interfaz gráfica ------------------

ventana = tk.Tk()
ventana.title("🏫 ITEL | MIA - PB - Python - Ejercicios U2 🧩")
ventana.geometry("450x300")
ventana.resizable(False, False)

ttk.Label(ventana, text="Ingrese palabras separadas por comas:").pack(pady=10)
entry_palabras = ttk.Entry(ventana, width=50)
entry_palabras.pack()

ttk.Button(ventana, text="Detectar Palíndromos", command=detectar_palindromos).pack(pady=10)

resultado_text = tk.StringVar()
ttk.Label(ventana, textvariable=resultado_text, justify="left", font=("Arial", 10)).pack(pady=10)

ventana.mainloop()