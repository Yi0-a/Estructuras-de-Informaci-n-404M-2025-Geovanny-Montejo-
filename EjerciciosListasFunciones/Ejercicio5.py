import random

n = int(input("Ingrese el tamano de la lista: "))
lista = []

numero = random.randint(5, 15)
lista.append(numero)

for i in range(1, n):
    anterior = lista[-1]              
    siguientenumero = (anterior // 10 + 1) * 10

    if anterior < siguientenumero:
        nuevo = random.randint(anterior + 1, siguientenumero)
        lista.append(nuevo)
    else:
        print(f"No se puede agregar otro numero despues de {anterior} porque alcanzamos la decena {siguientenumero}.")
        break

print("Lista generada:", lista)
