#Funcion para calcular

def calcular(valor1, valor2, parametro):
    
    
    resultado = 0


    if parametro == "+":
       resultado = valor1 + valor2
    elif parametro =="-":
         resultado = valor1 - valor2
    elif parametro == "*":  
        resultado = valor1 * valor2
    elif parametro == "/":
         parametro = valor1 / valor2
    else:
        print("EL parametro ingresado no es valido")
        #return "Si"

    print("El resultado de la operacion es:" ,resultado)
    #return "Ok"   

numero1 = 0
numero2 = 0
parametro = ""



mensaje = """
    Ingrese el simbolo de la operacion que quiere realizar:
    Sumar: +
    Restar: -
    Multiplicar: * 
    Dividir: /
"""

variable_salida = ""

"""while(variable_salida != "No"):
     parametro =  input(mensaje)
     variable_salida = calcular (numero1, numero2, parametro)"""

for i in range(1,5):
    numero1 = int(input("ingrese un numero:")) 
    numero2 = int(input("Ingrese el segundo numero a operar:")) 
    parametro = input(mensaje)
    
    calcular(numero1, numero2, parametro)    
         