# Tablas de verdad
print("---Tablas de verdad---")
A = True
B = False
C = True

if A and B:
     print("Verdadero") 
elif A and B or C:
     print("Segunda condicion")     
else:
     print("Falso")        

print("----Banco---")

edad = 0 # Cero, None, ""
ingresos = 0
reporte = ""
fiador = ""

edad = int(input("Ingrese su edad:\n "))
ingresos = float(input("Ingrese sus ingresos mensuales:\n"))

fiador = input("Tiene fiador?: (SI/NO\n").upper()
reporte =  input("Esta usted reportado?: (SI/NO\n").upper()

tieneEdad = (edad >= 18 and edad < 75)
#ingresos = (ingresos >= 2000000.0)

tieneFiador = None 

if fiador == "SI" or ingresos >= 2000000.0:
      tieneFiador = True
else: 
     tieneFiador = False

tieneReporte = (reporte == "SI")

creditoAprobado = tieneFiador and not tieneReporte and tieneEdad

if creditoAprobado:
     creditoAprobado = "Felicitaciones"
else:
     creditoAprobado = "Lo sentimos"

print("Edad:" , tieneEdad)
print("Fiador o Ingresos:" , tieneFiador)
print("Reporte: " , tieneReporte)
print(f"Estado de su credito  , {creditoAprobado}. :)")