#calculadora simple

def suma(Valor1, valor2):
    "Recibe dos parametros y los suma (+)"


    resultado = 0
    resultado = Valor1 + valor2
    print("Resultado de la suma: ", resultado)
    pass

def multiplicar(Valor1, valor2):
    "Recibe dos parametros y los multiplica (*)"


    resultado = 0
    resultado = Valor1 * valor2
    print("Resultado de la multiplicar: ", resultado)
    pass

def restar(Valor1, valor2):
    "Recibe dos parametros y los resta (-)"


    resultado = 0
    resultado = Valor1 - valor2
    print("Resultado de la resta: ", resultado)
    pass

def dividir(Valor1, valor2):
    "Recibe dos parametros y los divide (/)"

    resultado = 0
    resultado = Valor1 / valor2
    print("Resultado de la division: ", resultado)
    pass

numero1 = 0
numero2 = 0


mensaje = """
          por favor ingrese la operacion que quiere realizar:
          1) Sumar
          2) Restar
          3) Multiplicar
          4) Dividir
          """
operacion_usuario = 0
operacion_usuario = input(mensaje)

if operacion_usuario == 1:
    suma(numero1, numero2)
elif operacion_usuario ==2:
     multiplicar(numero1, numero2)
elif operacion_usuario  ==3:
     restar(numero1, numero2)
elif operacion_usuario ==4:
    dividir(numero1, numero2)
else:
    print("La opcion ingresadano es valida")    

    

