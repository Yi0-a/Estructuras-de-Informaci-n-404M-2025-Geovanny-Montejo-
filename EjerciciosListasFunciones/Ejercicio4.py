import random

n = int(input("Ingrese el tamano de la lista: "))
lista = []

while len(lista) < n:
    num = random.randint(5, 15) 
    if num not in lista:
        lista.append(num)
    else:
        print(f"El numero {num} ya esta en la lista, se descarta.")

print("Lista final sin repetidos:", lista)
