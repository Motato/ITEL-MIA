"""
Diseña un programa que, dados dos números, muestre por pantalla uno de estos	
mensajes: «El segundo es el cuadrado del	primero.», «E1 segundo es menor que	el	
cuadrado del primero.» o bien «El segundo es mayor que el cuadrado del primero.»,	
dependiendo	de la verificación	de	la	condición correspondiente al significado de 
cada mensaje.
"""

import sys
import tkinter as tk
from tkinter import messagebox

# Verificar codificación
print("Codificación por defecto:", sys.getdefaultencoding())

# Crear ventana principal
root = tk.Tk()
try:
    root.title("🏫 ITEL | MIA - PB - Ejercicios U2 🔍")
except UnicodeEncodeError:
    root.title("Comparador de Cuadrado")

root.geometry("400x300")
root.resizable(False, False)

# Variables
numero1 = tk.StringVar()
numero2 = tk.StringVar()

# Función para comparar
def comparar():
    try:
        n1 = float(numero1.get())
        n2 = float(numero2.get())
        cuadrado = n1 ** 2

        if n2 == cuadrado:
            mensaje = "✅ El segundo es el cuadrado del primero."
        elif n2 < cuadrado:
            mensaje = "📉 El segundo es menor que el cuadrado del primero."
        else:
            mensaje = "📈 El segundo es mayor que el cuadrado del primero."

        try:
            label_resultado.config(text=mensaje)
        except UnicodeEncodeError:
            label_resultado.config(text=mensaje.encode('ascii', 'ignore').decode())

    except ValueError:
        try:
            messagebox.showerror("Error", "⚠️ Ingrese valores numéricos válidos.")
        except UnicodeEncodeError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

# Función para reiniciar
def reiniciar():
    numero1.set("")
    numero2.set("")
    label_resultado.config(text="")

# Widgets
tk.Label(root, text="Ingrese el primer número:").pack(pady=5)
tk.Entry(root, textvariable=numero1).pack()

tk.Label(root, text="Ingrese el segundo número:").pack(pady=5)
tk.Entry(root, textvariable=numero2).pack()

tk.Button(root, text="Comparar", command=comparar).pack(pady=10)
label_resultado = tk.Label(root, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

tk.Button(root, text="Reiniciar", command=reiniciar).pack()

# Ejecutar la aplicación
root.mainloop()