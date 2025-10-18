""" Crear un programa con funciones para calcular el área de un triángulo, 
rectángulo, círculo, cubo y rombo. """
import tkinter as tk
from tkinter import ttk, messagebox
import math

# Funciones de área
def area_triangulo(base, altura): return (base * altura) / 2
def area_rectangulo(base, altura): return base * altura
def area_circulo(radio): return math.pi * radio ** 2
def area_cubo(arista): return 6 * arista ** 2
def area_rombo(D, d): return (D * d) / 2

# Diccionario de figuras y sus campos
figuras = {
    'Triángulo': {'func': area_triangulo, 'campos': ['Base', 'Altura']},
    'Rectángulo': {'func': area_rectangulo, 'campos': ['Base', 'Altura']},
    'Círculo': {'func': area_circulo, 'campos': ['Radio']},
    'Cubo': {'func': area_cubo, 'campos': ['Arista']},
    'Rombo': {'func': area_rombo, 'campos': ['Diagonal mayor', 'Diagonal menor']}
}

# Crear ventana principal
root = tk.Tk()
root.title("🏫 ITEL | MIA - PB - Python - Ejercicios U2 🧮")
root.geometry("400x400")

# Variables
figura_seleccionada = tk.StringVar()
entradas = {}

# Función para actualizar los campos según la figura
def actualizar_campos(*args):
    for widget in frame_campos.winfo_children():
        widget.destroy()
    entradas.clear()
    figura = figura_seleccionada.get()
    if figura in figuras:
        for campo in figuras[figura]['campos']:
            label = tk.Label(frame_campos, text=campo)
            label.pack()
            entry = tk.Entry(frame_campos)
            entry.pack()
            entradas[campo] = entry

# Función para calcular el área
def calcular_area():
    figura = figura_seleccionada.get()
    if figura not in figuras:
        messagebox.showerror("Error", "Seleccione una figura válida.")
        return
    try:
        valores = [float(entradas[campo].get()) for campo in figuras[figura]['campos']]
        resultado = figuras[figura]['func'](*valores)  # ✅ Llamada a la función con argumentos
        messagebox.showinfo("Resultado", f"Área del {figura}: {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

# Widgets
label_titulo = tk.Label(root, text="Calculadora de Áreas", font=("Arial", 16))
label_titulo.pack(pady=10)

combo_figuras = ttk.Combobox(root, textvariable=figura_seleccionada, values=list(figuras.keys()))
combo_figuras.pack()
combo_figuras.bind("<<ComboboxSelected>>", actualizar_campos)

frame_campos = tk.Frame(root)
frame_campos.pack(pady=10)

btn_calcular = tk.Button(root, text="Calcular Área", command=calcular_area)
btn_calcular.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()