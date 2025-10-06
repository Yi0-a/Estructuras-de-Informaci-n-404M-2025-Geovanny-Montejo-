import random

# Creo clase nodo 
class Nodo:
    def __init__(self, dato, puntero):
        self.dato = dato
        self.puntero = puntero

# Creo la lista 
class ListaEnlazada:
    def __init__(self):
        # creo el n0/cabeza
        self.cabeza = Nodo(None, None)

    def agregar_nodo(self, dato):
        nuevo = Nodo(dato, None)
        actual = self.cabeza

        if actual.dato is None:
            self.cabeza = nuevo
        else:
            # Hago el recorrido
            while actual.puntero is not None:
                actual = actual.puntero
            actual.puntero = nuevo

    def mostrar(self):
        actual = self.cabeza
        print("Lista enlazada:")
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.puntero
        print("None")

    def sumar(self):
        total = 0
        actual = self.cabeza
        while actual is not None:
            total += actual.dato
            actual = actual.puntero
        return total

    def promedio(self):
        total = 0
        contador = 0
        actual = self.cabeza
        while actual is not None:
            total += actual.dato
            contador += 1
            actual = actual.puntero
        return total / contador if contador > 0 else 0

    def maximo(self):
        if self.cabeza is None or self.cabeza.dato is None:
            return None
        max_val = self.cabeza.dato
        actual = self.cabeza.puntero
        while actual is not None:
            if actual.dato > max_val:
                max_val = actual.dato
            actual = actual.puntero
        return max_val

    def minimo(self):
        if self.cabeza is None or self.cabeza.dato is None:
            return None
        min_val = self.cabeza.dato
        actual = self.cabeza.puntero
        while actual is not None:
            if actual.dato < min_val:
                min_val = actual.dato
            actual = actual.puntero
        return min_val


lista = ListaEnlazada()

cantidad = random.randint(5, 15)
for _ in range(cantidad):
    valor = random.randint(0, 100)
    lista.agregar_nodo(valor)

print(f"Se crearon {cantidad} nods")
lista.mostrar()

print(f"Suma de los valores: {lista.sumar()}")
print(f"Promedio de los valores: {lista.promedio()}")
print(f"Valor máximo: {lista.maximo()}")
print(f"Valor mínimo: {lista.minimo()}")
