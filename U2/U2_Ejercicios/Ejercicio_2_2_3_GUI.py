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
import tkinter as tk
from tkinter import messagebox, scrolledtext

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

def mostrar_desglose():
    entrada = entry_cantidad.get()
    try:
        cantidad = int(entrada)
        if cantidad < 0:
            messagebox.showerror("Error", "⚠️ La cantidad debe ser positiva.")
            return
        resultado = calcular_desglose(cantidad)
        texto_resultado.config(state='normal')
        texto_resultado.delete("1.0", tk.END)
        try:
            texto_resultado.insert(tk.END, f"🔍 Desglose de {cantidad} €:\n\n")
        except UnicodeEncodeError:
            texto_resultado.insert(tk.END, f"Desglose de {cantidad} €:\n\n")
        for valor, tipo, unidades in resultado:
            palabra = tipo + ("s" if unidades > 1 else "")
            texto_resultado.insert(tk.END, f"{unidades} {palabra} de {valor} euros.\n")
        texto_resultado.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "⚠️ Ingrese un número entero válido.")

def reiniciar():
    entry_cantidad.delete(0, tk.END)
    texto_resultado.config(state='normal')
    texto_resultado.delete("1.0", tk.END)
    texto_resultado.config(state='disabled')

def salir():
    root.destroy()

# Crear ventana principal
root = tk.Tk()
try:
    root.title("🏫 ITEL | MIA - PB - Ejercicios U2 💶 Desglose de Euros")
except UnicodeEncodeError:
    root.title("Desglose de Euros")

root.geometry("420x400")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Ingrese la cantidad exacta de euros:", font=("Arial", 12)).pack(pady=10)
entry_cantidad = tk.Entry(root, font=("Arial", 12), justify="center")
entry_cantidad.pack()

tk.Button(root, text="Calcular Desglose", command=mostrar_desglose).pack(pady=10)

texto_resultado = scrolledtext.ScrolledText(root, width=40, height=10, font=("Arial", 11), state='disabled')
texto_resultado.pack(pady=10)

frame_botones = tk.Frame(root)
frame_botones.pack(pady=5)

tk.Button(frame_botones, text="Reiniciar", command=reiniciar, width=15).pack(side="left", padx=10)
tk.Button(frame_botones, text="Salir", command=salir, width=15).pack(side="right", padx=10)

# Ejecutar la aplicación
root.mainloop()

