import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

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

if __name__ == "__main__":
    pass