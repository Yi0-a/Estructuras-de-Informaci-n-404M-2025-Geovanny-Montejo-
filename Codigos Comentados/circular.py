# Clase Nodo, representa un nodo en la lista
class Nodo:
    def __init__(self, dato):
        self.dato = dato      # Guarda el valor del nodo
        self.siguiente = None       # Apunta al siguiente nodo (al inicio es None)

# Clase Circular, representa una lista circular enlazada
class Circular:
    def __init__(self):
        self.primero = None    # Referencia al primer nodo
        self.cont = 0      # Contador para llevar control de los elementos

    # Metodo para agregar un nuevo nodo a la lista
    def agregar(self, dato):
        nuevo = Nodo(dato)        # Se crea un nuevo nodo con el dato que llega
        if not self.primero:       # Si la lista esta vacia, este sera el primer nodo
            self.primero = nuevo   # El nuevo nodo se vuelve el primero
            nuevo.siguiente = self.primero  # Como es circular, se apunta a si mismo
        else:
            actual = self.primero
            # Recorremos hasta encontrar el ultimo nodo (el que apunta al primero)
            while actual.siguiente != self.primero:
                actual = actual.siguiente
                self.cont += 1        # Contamos los nodos mientras avanzamos
            # Al salir del ciclo, estamos en el ultimo nodo
            actual.siguiente = nuevo     # Lo conectamos con el nuevo nodo
            nuevo.siguiente = self.primero   # El nuevo apunta al primero para cerrar el ciclo
            self.cont += 1    # Aumentamos el total de nodos agregados

    # Metodo para mostrar los datos de la lista
    def mostrar(self):
        actual = self.primero
        i = 0
        # Recorremos hasta mostrar todos los nodos que agregamos (basado en el contador)
        while actual and i < self.cont:
            print(actual.dato)    # Mostramos el dato del nodo actual
            actual = actual.siguiente  # Pasamos al siguiente nodo
            i += 1

# Creamos una lista circular y agregamos algunos valores
k = Circular()
k.agregar(12)
k.agregar(9)
k.agregar(88)
k.agregar(8800)
k.agregar(9988)

# Mostramos los elementos de la lista
k.mostrar()
