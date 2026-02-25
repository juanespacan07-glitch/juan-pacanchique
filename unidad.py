lista = [1, 2, 3, 4, 5, 6, 7, 8, 9,] #lista

for x in lista:
    print(x)

print("------------------------")

tamaño_lista = len(lista)

i = 0
while(True):
    if i >= tamaño_lista:
        break
    print(lista[i])
    i += 1
    
