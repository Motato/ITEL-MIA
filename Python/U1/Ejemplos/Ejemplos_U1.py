import tkinter as tk
from tkinter import ttk

def mostrar_resultado(widget, texto):
    widget.delete("1.0", tk.END)
    widget.insert(tk.END, texto)

root = tk.Tk()
root.title("ITEL | MIA - Programación básica - Python - Ejemplos U1")
root.geometry("700x700")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# ---------------------- Ejemplo 1 ----------------------
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Ejemplo 1")
text1 = tk.Text(tab1, height=5)
text1.pack()
tk.Button(tab1, text="Ejecutar", command=lambda: mostrar_resultado(text1, "Hola Mundo")).pack()

# ---------------------- Ejemplo 2 ----------------------
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Ejemplo 2")
text2 = tk.Text(tab2, height=5)
text2.pack()
def ejemplo2():
    msg = "Hola Mundo"
    mostrar_resultado(text2, f"{msg}\n{msg[::-1]}")
tk.Button(tab2, text="Ejecutar", command=ejemplo2).pack()

# ---------------------- Ejemplo 3 ----------------------
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Ejemplo 3")
tk.Label(tab3, text="Largo:").pack()
entry_largo = tk.Entry(tab3)
entry_largo.pack()
tk.Label(tab3, text="Ancho:").pack()
entry_ancho = tk.Entry(tab3)
entry_ancho.pack()
text3 = tk.Text(tab3, height=5)
text3.pack()
def ejemplo3():
    try:
        largo = float(entry_largo.get())
        ancho = float(entry_ancho.get())
        area = largo * ancho
        mostrar_resultado(text3, f"Área del rectángulo: {area:.2f}")
    except:
        mostrar_resultado(text3, "Ingresa valores numéricos válidos.")
tk.Button(tab3, text="Calcular Área", command=ejemplo3).pack()

# ---------------------- Ejemplo 4 ----------------------
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Ejemplo 4")
text4 = tk.Text(tab4, height=10)
text4.pack()
def ejemplo4():
    resultado = (
        f"Suma: {12 + 67}\n"
        f"Resta: {89 - 4}\n"
        f"Multiplicación: {9 * 7}\n"
        f"División: {35 / 5}\n"
        f"Residuo: {40 % 5}\n"
        f"División entera: {40 // 7}\n"
        f"Potencia: {5 ** 2}\n"
        f"Jerarquía: {3 - 2 + 4 * 10}"
    )
    mostrar_resultado(text4, resultado)
tk.Button(tab4, text="Ejecutar Operaciones", command=ejemplo4).pack()

# ---------------------- Ejemplo 5 ----------------------
tab5 = ttk.Frame(notebook)
notebook.add(tab5, text="Ejemplo 5")
tk.Label(tab5, text="Nombre:").pack()
entry_nombre = tk.Entry(tab5)
entry_nombre.pack()
tk.Label(tab5, text="Apellido:").pack()
entry_apellido = tk.Entry(tab5)
entry_apellido.pack()
text5 = tk.Text(tab5, height=5)
text5.pack()
def ejemplo5():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    mostrar_resultado(text5, f"{nombre} {apellido}")
tk.Button(tab5, text="Mostrar Nombre Completo", command=ejemplo5).pack()

# ---------------------- Ejemplo 6 ----------------------
tab6 = ttk.Frame(notebook)
notebook.add(tab6, text="Ejemplo 6")
tk.Label(tab6, text="Frase:").pack()
entry_frase = tk.Entry(tab6)
entry_frase.pack()
text6 = tk.Text(tab6, height=5)
text6.pack()
def ejemplo6():
    frase = entry_frase.get()
    mostrar_resultado(text6, f"Longitud: {len(frase)}")
tk.Button(tab6, text="Calcular", command=ejemplo6).pack()

# ---------------------- Ejemplo 7 ----------------------
tab7 = ttk.Frame(notebook)
notebook.add(tab7, text="Ejemplo 7")
text7 = tk.Text(tab7, height=10)
text7.pack()
def ejemplo7():
    letras = ["a","b","c","d","e","f","g"]
    numeros = [1,2,8,5,6]
    original = f"Letras: {letras}\nNúmeros: {numeros}"
    letras[2:5] = []
    modificado1 = f"Letras sin c,d,e: {letras}"
    letras[1:2] = ['B','F']
    modificado2 = f"Letras con B,F: {letras}"
    resultado = (
        f"{original}\n{modificado1}\n{modificado2}\n"
        f"Tamaño letras: {len(letras)}\nTamaño números: {len(numeros)}"
    )
    mostrar_resultado(text7, resultado)
tk.Button(tab7, text="Ejecutar", command=ejemplo7).pack()

# ---------------------- Ejemplo 8 ----------------------
tab8 = ttk.Frame(notebook)
notebook.add(tab8, text="Ejemplo 8")
tk.Label(tab8, text="Base:").pack()
entry_base = tk.Entry(tab8)
entry_base.pack()
tk.Label(tab8, text="Altura:").pack()
entry_altura = tk.Entry(tab8)
entry_altura.pack()
text8 = tk.Text(tab8, height=5)
text8.pack()
def ejemplo8():
    try:
        b = float(entry_base.get())
        h = float(entry_altura.get())
        area = (b * h) / 2
        mostrar_resultado(text8, f"Área del triángulo: {area:.2f}")
    except:
        mostrar_resultado(text8, "Ingresa valores válidos.")
tk.Button(tab8, text="Calcular", command=ejemplo8).pack()

# ---------------------- Ejemplo 9 ----------------------
tab9 = ttk.Frame(notebook)
notebook.add(tab9, text="Ejemplo 9")
tk.Label(tab9, text="Nombre en minúsculas:").pack()
entry_minus = tk.Entry(tab9)
entry_minus.pack()
tk.Label(tab9, text="Nombre en mayúsculas:").pack()
entry_mayus = tk.Entry(tab9)
entry_mayus.pack()
text9 = tk.Text(tab9, height=5)
text9.pack()
def ejemplo9():
    nombre_min = entry_minus.get()
    nombre_may = entry_mayus.get()
    resultado = f"Mayúsculas: {nombre_min.upper()}\nMinúsculas: {nombre_may.lower()}"
    mostrar_resultado(text9, resultado)
tk.Button(tab9, text="Convertir", command=ejemplo9).pack()

# ---------------------- Ejemplo 10 ----------------------
tab10 = ttk.Frame(notebook)
notebook.add(tab10, text="Ejemplo 10")
entries_notas = []
for i in range(5):
    tk.Label(tab10, text=f"Calificación {i+1}:").pack()
    entry = tk.Entry(tab10)
    entry.pack()
    entries_notas.append(entry)
text10 = tk.Text(tab10, height=8)
text10.pack()
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)
def ejemplo10():
    try:
        notas = [float(e.get()) for e in entries_notas]
        promedio = calcular_promedio(notas)
        estado = "Aprobado" if promedio >= 70 else "Reprobado"
        resultado = (
            f"Calificaciones: {notas}\n"
            f"Promedio: {promedio:.2f}\n"
            f"Resultado: {estado}"
        )
        mostrar_resultado(text10, resultado)
    except:
        mostrar_resultado(text10, "Ingresa 5 calificaciones válidas.")
tk.Button(tab10, text="Calcular Promedio", command=ejemplo10).pack()

root.mainloop()