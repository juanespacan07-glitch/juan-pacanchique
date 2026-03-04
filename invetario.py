def main():
    
    inventario = []

    while True:
        opcion = input("Seleccione una opcion")
        
        if opcion == "1":
            print("---NUEVO PRODUCTO---")
            nombre = input("Nombre: ")

            try:
                precio = float(input("Ingrese el precio: "))
                stock = int(input("ingrese la cantiad: "))
            
                producto = {
                    "Nombre" : nombre,
                    "Precio" : precio,
                    "cantidad" : stock
                }

                inventario.append(producto)

            except ValueError:
                print("Error, el precio y stock deben ser numeros.")

        elif opcion =="2":
            print("---INVENTARIO ACTUAL---")

            if len(inventario) == 0:
                print("inventario vacio.")
            else:
                for item in inventario:
                    print(f"Producto: {item["Nombre"]}, el precio es {item["Precio"]} y su stock es de: {item["Cantidad"]}")    
       
        elif opcion =="3":
            busqueda = input("Ingrese el nombre a buscar: ").lower()
            encontrar = False

            for item in inventario:
                if item ["Nombre"].lower() == busqueda:
                    print(f"Encontrado: Precio ${item["Precio"]} - Stock: {item["Cantidad"]}")
                    encontrar = True
                    break
            
            if not encontrar:
                print("Producto no encontrado")

        elif opcion == "4":

            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intente de nuevo.")                

def menu():
    print("INICIO EL PROGRAMA")
    print("-----GESTION DE INVENTARIOS-----")
    print("1. Agrege el producto")
    print("2. Ver inventario completo")
    print("3.Buscar producto")
    print("4.Salir")

if __name__=="__main__":
    main()
