import random

def suma_lista(lista):
    return sum(lista)

def mayor_lista(lista):
    return max(lista)

def menor_lista(lista):
    return min(lista)

def promedio_lista(lista):
    return sum(lista) / len(lista)

def contar_pares(lista):
    return sum(1 for num in lista if num % 2 == 0)

def contar_impares(lista):
    return sum(1 for num in lista if num % 2 != 0)

def imprimir_menu():
    print("\n ---------- MENU ------------")
    print("1. Mostrar listas")
    print("2. Cual lista tiene la suma mas alta")
    print("3. Cual lista tiene el numero mayor")
    print("4. Cual lista tiene el numero menor")
    print("5. Promedio conjunto de las dos listas")
    print("6. Promedio de cada lista y comparacion con el promedio conjunto")
    print("7. Cual lista tiene mayor cantidad de pares")
    print("8. Cual lista tiene mayor cantidad de impares")
    print("0. Salir")

n = int(input("Ingrese el tamano de las listas: "))

lista1 = []
lista2 = []
for i in range(n):
    lista1.append(random.randint(5, 15))
    lista2.append(random.randint(5, 15))

while True:
    imprimir_menu()
    opcion = input("Seleccione una opcion: ")

    match opcion:
        case "1":
            print("Lista 1:", lista1)
            print("Lista 2:", lista2)

        case "2":
            if suma_lista(lista1) > suma_lista(lista2):
                print("La lista 1 tiene la suma mas alta:", suma_lista(lista1))
            elif suma_lista(lista1) < suma_lista(lista2):
                print("La lista 2 tiene la suma mas alta:", suma_lista(lista2))
            else:
                print("Ambas listas tienen la misma suma:", suma_lista(lista1))

        case "3":
            if mayor_lista(lista1) > mayor_lista(lista2):
                print("La lista 1 tiene el numero mayor:", mayor_lista(lista1))
            elif mayor_lista(lista1) < mayor_lista(lista2):
                print("La lista 2 tiene el numero mayor:", mayor_lista(lista2))
            else:
                print("Ambas listas tienen el mismo numero mayor:", mayor_lista(lista1))

        case "4":
            if menor_lista(lista1) < menor_lista(lista2):
                print("La lista 1 tiene el numero menor:", menor_lista(lista1))
            elif menor_lista(lista1) > menor_lista(lista2):
                print("La lista 2 tiene el numero menor:", menor_lista(lista2))
            else:
                print("Ambas listas tienen el mismo numero menor:", menor_lista(lista1))

        case "5":
            conjunto = lista1 + lista2
            print("Promedio conjunto:", promedio_lista(conjunto))

        case "6":
            conjunto = lista1 + lista2
            prom_conjunto = promedio_lista(conjunto)
            prom1 = promedio_lista(lista1)
            prom2 = promedio_lista(lista2)

            print("Promedio conjunto:", prom_conjunto)
            print("Promedio lista 1:", prom1,)
            print("Promedio lista 2:", prom2,)

        case "7":
            pares1 = contar_pares(lista1)
            pares2 = contar_pares(lista2)
            if pares1 > pares2:
                print("La lista 1 tiene mas pares:", pares1)
            elif pares2 > pares1:
                print("La lista 2 tiene mas pares:", pares2)
            else:
                print("Ambas listas tienen la misma cantidad de pares:", pares1)

        case "8":
            impares1 = contar_impares(lista1)
            impares2 = contar_impares(lista2)
            if impares1 > impares2:
                print("La lista 1 tiene mas impares:", impares1)
            elif impares2 > impares1:
                print("La lista 2 tiene mas impares:", impares2)
            else:
                print("Ambas listas tienen la misma cantidad de impares:", impares1)

        case "0":
            print("Fin del programa")
            break

