 # Programa para gestionar calificaciones en Python

def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

# Lista vacía para almacenar calificaciones
calificaciones = []

# Pedir 5 calificaciones
for i in range(5):
    nota = float(input(f"Ingrese la calificación {i+1}: "))
    calificaciones.append(nota)

# Calcular promedio
promedio = calcular_promedio(calificaciones)

print("\nCalificaciones ingresadas:", calificaciones)
print("Promedio:", promedio)

# Evaluar resultado
if promedio >= 70:
    print("Resultado: Aprobado")
else:
    print("Resultado: Reprobado")