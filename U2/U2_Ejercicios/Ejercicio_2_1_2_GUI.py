"""
Diseña una función llamada convertir temperatura (valor, escala) que reciba un
valor numérico y una escala de conversión ("C" para Celsius, "F" para Fahrenheit o
"K" para Kelvin).
"""
import tkinter as tk
from tkinter import ttk

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
    if not isinstance(valor, (int, float)):
        return "⚠️ El valor debe ser numérico."

    origen = origen.strip().upper()
    destino = destino.strip().upper()

    if origen not in TO_CELSIUS or destino not in FROM_CELSIUS:
        return "❌ Escalas no válidas. Usa 'C', 'F' o 'K'."

    try:
        temp_c = TO_CELSIUS[origen](valor)
        return FROM_CELSIUS[destino](temp_c)
    except Exception as e:
        return f"⚠️ Error inesperado: {e}"

# ---------------- GUI ----------------

def calcular_conversion():
    try:
        valor = float(entry_valor.get())
        origen = combo_origen.get()
        destino = combo_destino.get()
        resultado = convertir_temperatura(valor, origen, destino)

        if isinstance(resultado, (int, float)):
            resultado_text.set(f"{valor:.2f}°{origen} = {resultado:.2f}°{destino}")
        else:
            resultado_text.set(resultado)
    except ValueError:
        resultado_text.set("⚠️ Entrada inválida. Ingrese un número válido.")

ventana = tk.Tk()
ventana.title("🏫 ITEL | MIA - PB - Python - Ejercicios U2 🌡️")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Entrada de valor
ttk.Label(ventana, text="Valor de temperatura:").pack(pady=5)
entry_valor = ttk.Entry(ventana, width=20)
entry_valor.pack()

# Escala de origen
ttk.Label(ventana, text="Escala de origen:").pack(pady=5)
combo_origen = ttk.Combobox(ventana, values=["C", "F", "K"], state="readonly", width=5)
combo_origen.set("C")
combo_origen.pack()

# Escala de destino
ttk.Label(ventana, text="Escala de destino:").pack(pady=5)
combo_destino = ttk.Combobox(ventana, values=["C", "F", "K"], state="readonly", width=5)
combo_destino.set("F")
combo_destino.pack()

# Botón de conversión
ttk.Button(ventana, text="Convertir", command=calcular_conversion).pack(pady=10)

# Resultado
resultado_text = tk.StringVar()
ttk.Label(ventana, textvariable=resultado_text, font=("Arial", 12), foreground="blue").pack(pady=10)

ventana.mainloop()