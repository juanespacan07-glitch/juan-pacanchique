
estudiantes = [
{"nombre" : "Juan", "Notas":[3.0, 4.5, 4.0]},
{"nombre" : "Myraa", "Notas":[4.0, 5.0, 3.5]},
{"nombre" : "Ryu", "Notas":[3.0, 4.2, 3.5]}
]
print("---Datos cargados---")
print(f"Total de estudiantes: {len(estudiantes)}")

def reporte(estudiantes):
    print("---Reporte Final---")
    for est in estudiantes:
        suma = sum(est["Notas"])
        prom = suma / len(est["Notas"])

        if prom >=3.0:
           estado = "Aprobado"
        else:
            estado = "Reprobado"

        print(f"estudiantes: {est["nombre"]} su estado es {estado}")

reporte(estudiantes)