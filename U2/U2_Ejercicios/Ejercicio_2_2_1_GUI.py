import tkinter as tk
from tkinter import ttk

def salario_base(horas, tarifa):
    return min(horas, 40) * tarifa

def salario_doble(horas, tarifa):
    return min(max(horas - 40, 0), 5) * tarifa * 2

def salario_triple(horas, tarifa):
    return max(horas - 45, 0) * tarifa * 3

def actualizar_valores_slider(*args):
    valor_horas.set(f"{slider_horas.get():.0f} horas")
    valor_tarifa.set(f"${slider_tarifa.get():.0f} por hora")

def calcular_salario_gui():
    horas = slider_horas.get()
    tarifa = slider_tarifa.get()

    base = salario_base(horas, tarifa)
    doble = salario_doble(horas, tarifa)
    triple = salario_triple(horas, tarifa)
    total = base + doble + triple

    label_base.config(text=f"Salario normal (hasta 40h): ${base:.2f}")
    label_doble.config(text=f"Horas extra al doble (hasta 5h): ${doble:.2f}")
    label_triple.config(text=f"Horas extra al triple: ${triple:.2f}")
    label_total.config(text=f"💰 Salario total: ${total:.2f}")

# Crear ventana
ventana = tk.Tk()
ventana.title("🏫 ITEL | MIA - PB - Python - Ejercicios U2 🧮")
ventana.geometry("420x400")
ventana.resizable(False, False)

# Variables para mostrar valores
valor_horas = tk.StringVar()
valor_tarifa = tk.StringVar()

# Slider de horas trabajadas
ttk.Label(ventana, text="Horas trabajadas:").pack(pady=5)
slider_horas = ttk.Scale(ventana, from_=0, to=80, orient="horizontal", length=300, command=actualizar_valores_slider)
slider_horas.set(40)
slider_horas.pack()
ttk.Label(ventana, textvariable=valor_horas, font=("Arial", 10, "italic")).pack()

# Slider de salario por hora
ttk.Label(ventana, text="Salario por hora ($):").pack(pady=5)
slider_tarifa = ttk.Scale(ventana, from_=10, to=1000, orient="horizontal", length=300, command=actualizar_valores_slider)
slider_tarifa.set(100)
slider_tarifa.pack()
ttk.Label(ventana, textvariable=valor_tarifa, font=("Arial", 10, "italic")).pack()

# Botón de cálculo
ttk.Button(ventana, text="Calcular salario", command=calcular_salario_gui).pack(pady=10)

# Etiquetas educativas
label_base = ttk.Label(ventana, text="Salario normal: $0.00")
label_base.pack()

label_doble = ttk.Label(ventana, text="Horas dobles: $0.00")
label_doble.pack()

label_triple = ttk.Label(ventana, text="Horas triples: $0.00")
label_triple.pack()

label_total = ttk.Label(ventana, text="💰 Salario total: $0.00", font=("Arial", 12, "bold"))
label_total.pack(pady=10)

# Inicializar etiquetas de sliders
actualizar_valores_slider()

ventana.mainloop()