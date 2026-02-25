def main():
    print("INICIO PROGRAMA")
    Producto = {}

    nombre = input("Ingrese el nombre del producto:\n")
    precio = float(input("Ingrese el precio:\n"))
    cantidad = int(input("Ingrese la cantidad:\n"))


    Producto["Nombre"] = nombre
    Producto["precio"] = precio
    Producto["cantidad"] =cantidad
    print("El dicionario es:", Producto)

if __name__=="__main__":
    main()    