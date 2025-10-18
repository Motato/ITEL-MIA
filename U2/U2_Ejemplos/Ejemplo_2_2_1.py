# 2.2	Sentencias	if,	else	y	elif.
"""
Escriba un programa	 para verificar	 que la	 calificación de un	alumno sea	
aprobatoria, para ello el número que se ingrese debe ser mayor a un 7. 
"""
calificacion = float(input("Ingrese la calificación aprobatoria de un alumno: "))
if calificacion < 7:
    print("La calificación debe ser mayor que 6")
print(f"Ha escrito la calificación de: {calificacion}")