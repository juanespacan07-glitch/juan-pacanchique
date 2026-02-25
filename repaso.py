def main():
    print("inicio el programa")
    notas = []
    
    try:
        for i in range(1,4):
            print("paso" , i)
            nota = float(input("Ingrese la nota:\n"))  
            notas.append(nota)
            if nota < 3.0:
                print("Reprobado")
            elif nota < 4.0:
                print("Aceptable")
            else:
                print("Exelente")     

        print("Estas son las notas:", notas)

        tamanolista = len(notas)
        contador = 0
        sumanotas = 0
        while(contador <tamanolista):
            notawhile = notas[contador]
            sumanotas += notawhile
            contador = contador + 1
        promedio = sumanotas/tamanolista
        print("Su promedio es:", promedio)
    # exept ValueError
    #   print ("Falle por tipo de datos")
    
    except Exception as e:
        print("El programa fallo por otro problema")
    finally:
        print("El programa finalizo.")             

if __name__ =="__main__":    
   main()