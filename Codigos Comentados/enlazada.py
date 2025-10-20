# Clase Nodo, que representa cada elemento de la lista enlazada
class Nodo():
    def __init__(self, dato):
        self.dato = dato    # Guarda el dato que le pasamos
        self.siguiente = None   # Apunta al siguiente nodo, que al principio es None

# Clase Lista, que representa la lista enlazada simple
class Lista:
    def __init__(self):
        self.primero = None  # Al inicio la lista esta vacia, asi que primero es None

    # Metodo para agregar un nuevo nodo al final de la lista
    def agregar(self, dato):
        nuevo = Nodo(dato)  # Creamos un nuevo nodo con el dato que queremos
        if not self.primero:  # Si la lista esta vacia (primero es None)
            self.primero = nuevo  # el nuevo nodo es el primero de la lista
        else:
            actual = self.primero  # Si no esta vacia, recorremos la lista hasta el ultimo nodo
            while actual.siguiente:  # Mientras haya un siguiente nodo
                actual = actual.siguiente  # avanzamos al siguiente
            actual.siguiente = nuevo  # Cuando llegamos al ultimo nodo, le asignamos el nuevo nodo como siguiente
        return 1  # Devuelve 1 para indicar que se agrego bien

    # Metodo para eliminar un nodo que tenga el dato dado
    def eliminar(self, dato):
        actual = self.primero
        anterior = None
        # Buscamos el nodo con el dato que queremos eliminar
        while actual and actual.dato != dato:
            anterior = actual  # Guardamos el nodo anterior para poder enlazar despues
            actual = actual.siguiente  # Avanzamos al siguiente nodo
        if not actual:  # Si no encontramos el dato, no hacemos nada
            return
        if not anterior:  # Si el nodo a eliminar es el primero
            self.primero = actual.siguiente  # movemos la cabeza al siguiente nodo
        else:
            anterior.siguiente = actual.siguiente  # Si no es el primero, saltamos el nodo a eliminar

    # Metodo para imprimir todos los datos de la lista
    def imprimir(self):
        actual = self.primero
        while actual:
            print(actual.dato)  # Imprimimos el dato del nodo actual
            actual = actual.siguiente  # Avanzamos al siguiente nodo

# Creamos una lista llamada lili
lili = Lista()

# Agregamos algunos datos
lili.agregar('k')
lili.agregar(999)
lili.agregar(1000)

