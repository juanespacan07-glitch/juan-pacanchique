def saludar(nombre):
    print("Hola Mundo", nombre)

saludar("Juan")
saludar("Esteban")

for numero in range(1,3):
    print(numero)
    print("---------------")
    nombre = input("ingrese su nombre: ")
    if nombre.strip().lower() == "JOJO":
       break
    saludar(nombre)

while(True):
   print("Aqui inicia el while")
   nombre = input("ingrese su nombre:")

     #upper() pasar a mayusculas
     #lower() pasar a minusculas
     #strip() quitar espacios  
   if nombre.strip() == "salir":
       break
   saludar(nombre)