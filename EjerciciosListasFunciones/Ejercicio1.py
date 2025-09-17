import random
import statistics

def imprimir_lista(lista):
    print("Lista original:", lista)

def suma_lista(lista):
    return sum(lista)

def promedio_lista(lista):
    return sum(lista) / len(lista)

def mayor_lista(lista):
    return max(lista)

def menor_lista(lista):
    return min(lista)

def ordenar_ascendente(lista):
    return sorted(lista)

def ordenar_descendente(lista):
    return sorted(lista, reverse=True)

def moda_lista(lista):
    try:
        return statistics.mode(lista)
    except statistics.StatisticsError:
        return "No hay moda unica"

def mediana_lista(lista):
    return statistics.median(lista)

def buscar_numero(lista, num):
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == num:
            posiciones.append(i)
    return posiciones

def imprimir_menu():
    print("\n ---------- MENU ------------")
    print("1. Imprimir arreglo original")
    print("2. Suma")
    print("3. Promedio")
    print("4. Mayor")
    print("5. Menor")
    print("6. Ordenar ascendente")
    print("7. Ordenar descendente")
    print("8. Moda")
    print("9. Mediana")
    print("10. Buscar numero")
    print("0. Salir")


n = int(input("Ingrese el tamano de la lista: "))
lista = []
for i in range(n):
    lista.append(random.randint(5, 15))

while True:
    imprimir_menu()
    opcion = input("Seleccione una opcion: ")

    match opcion:
        case "1":
            imprimir_lista(lista)
        case "2":
            print("Suma:", suma_lista(lista))
        case "3":
            print("Promedio:", promedio_lista(lista))
        case "4":
            print("Mayor:", mayor_lista(lista))
        case "5":
            print("Menor:", menor_lista(lista))
        case "6":
            print("Lista en orden ascendente:", ordenar_ascendente(lista))
        case "7":
            print("Lista en orden descendente:", ordenar_descendente(lista))
        case "8":
            print("Moda:", moda_lista(lista))
        case "9":
            print("Mediana:", mediana_lista(lista))
        case "10":
            num = int(input("Ingrese el numero a buscar: "))
            posiciones = buscar_numero(lista, num)
            if posiciones:
                print(f"El numero {num} esta en las posiciones {posiciones} y aparece {len(posiciones)} vez/veces.")
            else:
                print(f"El numero {num} no esta en la lista.")
        case "0":
            print("Fin del programa")
            break

