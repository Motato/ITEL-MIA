"""
Hacer un programa, que calcule el salario de los trabajadores de una empresa, el
cual consiste en lo siguiente: Por las primeras 40 horas trabajadas recibe un salario
normal. Por las siguientes 5 horas el doble y por las restantes el triple. El programa
debe pedir el número de horas trabajadas y el salario por horas de trabajo.
"""

def salario_base(horas, tarifa):
    return min(horas, 40) * tarifa

def salario_doble(horas, tarifa):
    return min(max(horas - 40, 0), 5) * tarifa * 2

def salario_triple(horas, tarifa):
    return max(horas - 45, 0) * tarifa * 3

def calcular_salario(horas, tarifa):
    if horas < 0 or tarifa < 0:
        raise ValueError("Las horas y el salario deben ser positivos.")
    
    base = salario_base(horas, tarifa)
    doble = salario_doble(horas, tarifa)
    triple = salario_triple(horas, tarifa)
    total = base + doble + triple

    print(f"🧾 Desglose del salario:")
    print(f" - Salario normal (hasta 40h): ${base:.2f}")
    print(f" - Horas extra al doble (hasta 5h): ${doble:.2f}")
    print(f" - Horas extra al triple: ${triple:.2f}")
    print(f"💰 Salario total: ${total:.2f}")
    return total

if __name__ == "__main__":
    try:
        horas = float(input("Ingrese las horas trabajadas: "))
        tarifa = float(input("Ingrese el salario por hora: "))
        calcular_salario(horas, tarifa)
    except ValueError as e:
        print(f"⚠️ Error: {e}")
        

