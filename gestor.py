def menu():
    print("---menu---")
    print("Bienvenidos por favor ingrese una opsion: ")
    opciones = """ 1)Agregar productos
                   2)Ver inventario
                   3)consultar
                   4)salir
    """
    print(opciones)

def main():
    inventario = [] #Guardar los productos
    while(True):
        menu()
        opcion = int(input("Selecione una opcion:\n"))
   
        if opcion == 1:
           print("NUEVO PRODUCTO")
           nombre = input("Ingrese el nombre: ")
           precio = float(input("Ingrese el precio: "))
           cantidad = int(input("Ingrese la cantidad: "))
           producto ={"Nombre": nombre,
                      "precio": precio}
           producto["Cantidad"] = cantidad
           
           inventario.append(producto)
           print("Producto guardado con exito")

        elif opcion == 2:
            print("Inventario actual")
            

            if len(inventario) == 0:
                print("Inventario vacio. ")
            else:
                for item in inventario:
                    print(f"Nombre del producto {item["Nombre"]}\
                          y el precio es {item["precio"]} y su \
                            Cantidad es {item["Cantidad"]}")
            print(inventario)

        elif opcion == 3:
            pass
        elif opcion == 4:
            break
        else:
            print("opcion no valida")

if __name__  == "__main__":
   main()