# Librerias necesarias para el funcionamiento de los programas
import math
import tkinter as tk
from tkinter import ttk, messagebox

# Función 1: Conversión de temperatura
def conversion_temperatura():
    try:
        celsius = float(entry_celsius.get())
        farenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.5
        label_temp_result.config(text=f"F: {farenheit:.2f} °F | K: {kelvin:.2f} K")
        messagebox.showinfo("Conversión", "¡Conversión de temperatura completada!")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido para Celsius.")

# Función 2: Operaciones con números
def operaciones_numeros():
    try:
        numero = float(entry_numero.get())
        doble = numero * 2
        triple = numero * 3
        raiz = numero ** 0.5
        label_operaciones_result.config(text=f"Doble: {doble:.2f}, Triple: {triple:.2f}, Raíz: {raiz:.2f}")
        messagebox.showinfo("Operaciones", "¡Cálculos completados!")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido.")

# Función 3: Calcular área y perímetro de un círculo
def calcular_radio():
    try:
        radio = float(entry_radio.get())
        # area = 3.1416 * (radio**2) # Sin math.pi
        area = math.pi * (radio**2)
        # perimetro = 3.1416 * (radio*2) # Sin math.pi
        perimetro = math.pi * (radio*2)
        label_radio_result.config(text=f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")
        messagebox.showinfo("Círculo", "¡Cálculo de círculo completado!")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido para el radio.")

# Función 4: Calculadora Geometrica
def calculadora_geometrica():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        radio = float(entry_radio_geo.get())

        # Triángulo equilátero
        area_triangulo = (base ** 2) / 2
        perimetro_triangulo = base * 3

        # Círculo
        area_circulo = math.pi * (radio ** 2)
        perimetro_circulo = 2 * math.pi * radio

        # Rectángulo
        area_rectangulo = base * altura
        perimetro_rectangulo = 2 * (base + altura)

        resultado = (
            f"🔺 Triángulo equilátero:\nÁrea: {area_triangulo:.2f}, Perímetro: {perimetro_triangulo:.2f}\n\n"
            f"⚪ Círculo:\nÁrea: {area_circulo:.2f}, Perímetro: {perimetro_circulo:.2f}\n\n"
            f"▭ Rectángulo:\nÁrea: {area_rectangulo:.2f}, Perímetro: {perimetro_rectangulo:.2f}"
        )
        label_geo_result.config(text=resultado)
        messagebox.showinfo("Geometría", "¡Cálculos geométricos completados!")
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores válidos para base, altura y radio.")

# Crear ventana principal
root = tk.Tk()
root.title("ITEL | MIA - Programación básica - Python - Ejercicios U1")
root.geometry("500x500")

# Crear el contenedor de pestañas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Pestaña 1: Conversión de temperatura
tab_temp = ttk.Frame(notebook)
notebook.add(tab_temp, text="Temperatura")
tk.Label(tab_temp, text="Grados Celsius:").pack(pady=5)
entry_celsius = tk.Entry(tab_temp)
entry_celsius.pack()
tk.Button(tab_temp, text="Convertir", command=conversion_temperatura).pack(pady=5)
label_temp_result = tk.Label(tab_temp, text="Resultado temperatura")
label_temp_result.pack(pady=5)

# Pestaña 2: Operaciones con números
tab_operaciones = ttk.Frame(notebook)
notebook.add(tab_operaciones, text="Operaciones")
tk.Label(tab_operaciones, text="Número:").pack(pady=5)
entry_numero = tk.Entry(tab_operaciones)
entry_numero.pack()
tk.Button(tab_operaciones, text="Calcular", command=operaciones_numeros).pack(pady=5)
label_operaciones_result = tk.Label(tab_operaciones, text="Resultado operaciones")
label_operaciones_result.pack(pady=5)

# Pestaña 3: Círculo
tab_radio = ttk.Frame(notebook)
notebook.add(tab_radio, text="Círculo")
tk.Label(tab_radio, text="Radio:").pack(pady=5)
entry_radio = tk.Entry(tab_radio)
entry_radio.pack()
tk.Button(tab_radio, text="Calcular", command=calcular_radio).pack(pady=5)
label_radio_result = tk.Label(tab_radio, text="Resultado círculo")
label_radio_result.pack(pady=5)

# Pestaña 4: Geometría básica
tab_geo = ttk.Frame(notebook)
notebook.add(tab_geo, text="Geometría")

tk.Label(tab_geo, text="Base:").pack(pady=5)
entry_base = tk.Entry(tab_geo)
entry_base.pack()

tk.Label(tab_geo, text="Altura (para rectángulo):").pack(pady=5)
entry_altura = tk.Entry(tab_geo)
entry_altura.pack()

tk.Label(tab_geo, text="Radio (para círculo):").pack(pady=5)
entry_radio_geo = tk.Entry(tab_geo)
entry_radio_geo.pack()

tk.Button(tab_geo, text="Calcular Geometría", command=calculadora_geometrica).pack(pady=10)

label_geo_result = tk.Label(tab_geo, text="Resultados geométricos", justify="left")
label_geo_result.pack(pady=5)

# Ejecutar ventana
root.mainloop()