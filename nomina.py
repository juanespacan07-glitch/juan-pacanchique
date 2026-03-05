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
        
        print("Nombre de empleado %s y sueldo %d con auxilio de: %d" % (emp["Nombre"], sueldo_proporcional, auxilio))  

    print("-" *75)
    print(f"Total_ a pagar por la empresa: ${total_nomina:.2f}")
def registrar_empleado(lista_empleado):
    print("---REGISTRO DE EMPLEADOS---")

    nombre = input("Ingrese el nombre del empleado:\n")

    try:
       salario_base = float(input("Ingrese el salario mensual: "))
       dias_trabajados = int(input("Ingrese cantidad de dias (1-30): "))

       if dias_trabajados < 1 or dias_trabajados > 30:
           print("Cantidad de dias ingresados no valida")
           return
       
       empleado ={
           "Nombre": nombre,
            "Salario" : salario_base,
            "Dias" : dias_trabajados
       }

       lista_empleado.append(empleado)
       print("Empleado % registrado con exito" % (nombre))

    except ValueError:
        print("Error ingrese valores numericos validos para salario y dias.")
def main ():
    empleados = []

    while True:
        limpiar_pantalla()
        print("---Inicia programa----")
        print("1. Registrar empleado")
        print("2. Procesar nomina")
        print("3. salir")

        opcion = input("Selecciona una opcion:\n")

        if opcion == "1":
           registrar_empleado(empleados)
           input("Enter para volver")
        elif opcion == "2":
             calcular__nomina(empleados)
        elif opcion == "3":       
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()