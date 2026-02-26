
estudiantes = [
{"nombre" : "Juan", "Notas":[3.0, 4.5, 4.0]},
{"nombre" : "Myraa", "Notas":[4.0, 5.0, 3.5]},
{"nombre" : "Ryu", "Notas":[3.0, 4.2, 3.5]}
]
print("---Datos cargados---")
print(f"Total de estudiantes: {len(estudiantes)}")

def calcular_promedio(lista_notas):
    if len(lista_notas) ==0:
        return 0   

    suma = 0
    for nota in lista_notas:
      suma += nota

    promedio = suma / len(lista_notas)
    return promedio


print("Prueba promedio Myraa", calcular_promedio(estudiantes[1]["Notas"]))