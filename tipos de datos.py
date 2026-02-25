listatest = [1, 2, "Hola Mundo", 0.9, True] #lista
tuplatest = (1, 2, 3) #tupla, no se puede modificar
diccionario = {"Nombre": "Camilo",
                "Edad": 20, #Diccionario
                "Correo": "test@text.com"}

print(listatest[3]) #Hola Mundo
print(tuplatest[2]) #3
print(diccionario["Edad"]) #20

print("---Imprimiendo lista---")
for i in listatest:
    print(i)

print("---Imprimiendo tupla---")
for i in tuplatest:
    print(i)

print("---Imprimiendo Diccionario---")
for clave, valor in diccionario.items():
    print(f"Esta es la clave {clave} y este es el valor {valor}")    

print("---Imprimiendo lista while---")
tamanolista = len(listatest)
contador = 0
while(contador < tamanolista):
    print(listatest[contador])
    contador += 1    

print("---imprimiendo Diccionario while---")
claves = list(diccionario.keys())
lenClaves = len(claves)
i = 0
while(i < lenClaves):
    print("Esta es mi clave" , claves[i])
    print(f"Este valor: {diccionario[claves[i]]}")
    i +=1

    print("---Convirtiendo texto a la lista---")
    texto = "Hola Mundo, Bienvenidos"
    print(list(texto))

    print("---Trabajando con listas---")
    frutas = ["Pera" , "Manzana", "Fresas" , "Banana" , "Uva"]
    print(frutas[2]) #Fresas
    print(frutas[0:2]) #["Pera" , "manzanas"]
    print(frutas[-1]) # Uva
    print(frutas[-1:]) #["Uva"]
    print(frutas[:-1]) #['Pera', 'Manzana', 'Fresas', 'Banana']
    print(frutas[::2]) #['Pera', 'Fresas', 'Uva'] Cada 2 elementos

    frutas.pop()
    print("Quitas un elemento")
    print(frutas)
    frutas.append("mora")
    print(frutas)
    print("Agregamos un elemento")
    frutas.append("mora")
    print(frutas)
    print("Quita un elemento por indice")
    frutas.pop(1)
    print(frutas)
    print("Quito elemento por nombre")
    frutas.remove("Fresas")
    print(frutas)
    print("Agregar elemento por pocicion")
    frutas.insert(1, "Guanabana")
    print(frutas)
    print("Modificar elemento por pocicion")
    frutas[1] = "Kiwi"
    print(frutas)

    diccionario["Edad"] = 27, "correo@correo"    
    print(diccionario)
    print(frutas)
    print("Ver lista al reves")
    print(frutas[::-1])
    frutas.reverse() #modifica el texto
    print(frutas)
    frutas = reversed(frutas) #invierte un objeto
    print(list(frutas))
    texto2 = "".join(reversed(texto)) #Convierte un objeto -> stu
    print(texto2, texto)
    
    frutas2 = frutas
    #frutas2 
    print(frutas2, frutas)
    """----- Diccionario----- """
    print("---Diccionarios---")
    print(diccionario["Edad"])
    diccionario["Direccion"] = "Av Caracas"
    print(diccionario)
    diccionario["Edad"] = 20, 30
    print(diccionario)
    print(diccionario.get("Telefono" , "Esta clave no existe"))