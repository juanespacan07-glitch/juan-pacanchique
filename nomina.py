import os

TOPE_AUXILIO = 2000000
VALOR_AUXILIO = 160000
DEDUCCIONES = 0.08 # 8%

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def calcular__nomina(lista_empleados):
    print("---NOMINA GENERAL---")

    if not lista_empleados:
        print("No hay empleados registrados. ")
        return

    print("-" * 75)

    total_nomina = 0

    for emp in lista_empleados:

        sueldo_proporcional = (emp["Salario"] / 30) * emp["Dias"]
        auxilio = 0

        if emp["Salario"] < TOPE_AUXILIO:
            auxilio = (VALOR_AUXILIO / 30) * emp["Dias"]

        deducciones = sueldo_proporcional + DEDUCCIONES
        neto = sueldo_proporcional + deducciones
        total_nomina += neto # total_nomina = total_nomina + neto
        
        print("Nombre de empleado %s y sueldo %d con auxilio de: %d" % (emp["Nombre"]))  

    print("-" *75)
    print(f"Total_ a pagar por la empresa")

if __name__ == "__main__":
    pass