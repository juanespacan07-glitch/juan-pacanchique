
def calcular_area():
    
    base = None
    altura = 0

    resultado = 0

    """
    Esta funcion calcula el area de un rectangulo
    """

 
    base = None # Almaceno la base
    altura = 0 #Almaceno la altura
    resultado = 0 #variable para guardar el resultado
      
    #  variable para guardar el resultado

    base = input("Ingresa la base ")
    altura = input("Ingrese la altura: ")
    resultado = int(base) * int (altura)

    print("esta es el area", resultado)



    base = None # Almaceno la base 
    altura = 0 # Almaceno la altura

    base = int(input("Ingrese la base"))
    altura = int(input("Ingrese la altura"))

    calcular_area(base,altura) # Llamo a la funcion
