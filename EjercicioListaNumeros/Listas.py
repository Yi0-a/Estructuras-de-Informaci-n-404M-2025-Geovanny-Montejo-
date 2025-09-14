import random

cantidad = random.randint(5, 15)  
print(f"Cantidad de elementos: {cantidad}")

lista = []
for i in range(cantidad):
    lista.append(random.randint(1, 20)) 

print("Lista generada:", lista)

buscado = int(input("Ingrese el número que desea buscar: "))

posiciones = []

for i in range(len(lista)):
    if lista[i] == buscado:
        posiciones.append(i)

if len(posiciones) > 0:
    print(f"\nEl numero {buscado} Si esta en la lista.")
    print(f"Se encontro {len(posiciones)}")
    print("Posiciones donde aparece:", posiciones)
else:
    print(f"\nEl numero {buscado} NO esta en la lista.")
