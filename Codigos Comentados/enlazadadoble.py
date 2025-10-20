# Clase NodoDoble, que representa cada nodo de la lista doble
class NodoDoble:
    # El constructor crea el nodo con un dato y lo deja con el siguiente y anterior en None
    def __init__(self, dato):
        self.dato = dato   # Guarda el valor que le damos al nodo
        self.siguiente = None # Al principio no hay siguiente nodo
        self.anterior = None # Al principio no hay nodo anterior

# Clase ListaDoble, que representa la lista doblemente enlazada
class ListaDoble:
    def __init__(self):
        self.cabeza = None # Al principio no hay nodos, así que cabeza es None
        self.cola = None  # Y cola tampoco tiene un nodo

    # Este metodo sirve para agregar nodos a la lista
    def agregar(self, dato):
        nuevo = NodoDoble(dato) # Creamos un nuevo nodo con el dat

        # Si la lista está vacía (si la cabeza es None), el nuevo nodo será la cabeza y la cola
        if not self.cabeza:
            self.cabeza = nuevo # Primero se pone como cabeza
            self.cola = nuevo  # Y también como cola
        else:
            # Si ya hay nodos, el nuevo nodo se agrega al final
            self.cola.siguiente = nuevo  # El nodo que estaba en la cola ahora apunta al nuevo nodo
            nuevo.anterior = self.cola # El nuevo nodo apunta al anterior (la vieja cola)
            self.cola = nuevo  # Actualizamos la cola, ahora es el nuevo nodo

    # Este metodo recorre la lista de adelante hacia atrás, desde la cabeza hasta la cola
    def adelante(self):
        actual = self.cabeza  # Empezamos desde la cabeza de la lista
        while actual:
            print(actual.dato) # Imprimimos el dato del nodo actual
            actual = actual.siguiente  # Vamos al siguiente nodo
        print("None")  # Al final imprimimos None para indicar que ya no hay más nodos

    # Este metodo recorre la lista de atrás hacia adelante, desde la cola hasta la cabeza
    def atras(self):
        actual = self.cola  # Empezamos desde la cola
        while actual:
            print(actual.dato)  # Imprimimos el dato del nodo actual
            actual = actual.anterior  # Vamos al nodo anterior
        print("None")  # Al final imprimimos None para indicar que ya no hay más nodos

# Creamos una lista doble
l1 = ListaDoble()

# Agregamos datos a la lista
l1.agregar(456)
l1.agregar(444)
l1.agregar(555)
l1.agregar(678)

# Imprimimos la lista de adelante hacia atrás
l1.adelante()

# Imprimimos la lista de atrás hacia adelante
l1.atras()
