# Clase NodoDoble, representa un nodo de lista doblemente enlazada
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato          # Guarda el valor que le pasamos
        self.siguiente = None       # Apunta al nodo siguiente
        self.anterior = None    # Apunta al nodo anterior

# Clase ListaDoble, lista doblemente enlazada circular
class ListaDoble:
    def __init__(self):
        self.cabeza = None    # Primer nodo de la lista
        self.cola = None         # Ultimo nodo de la lista
        self.cont = 0           # Contador para saber cuantos nodos hay

    # Metodo para agregar nodos a la lista
    def agregar(self, dato):
        nuevo = NodoDoble(dato)      # Se crea un nodo nuevo con el dato que llega
        if not self.cabeza:      # Si la lista esta vacia  el nuevo nodo es la cabeza y tambien es la cola
            self.cabeza = nuevo     
            self.cola = nuevo       
        else:
            # Conectamos el nuevo nodo al final de la lista
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo    

        # Esto hace que la lista sea circular
        self.cola.siguiente = self.cabeza    # El ultimo apunta al primero y el primero apunta al ultimo
        self.cabeza.anterior = self.cola        

        self.cont += 1 # Aumentamos el contador de nodos

    # Metodo para recorrer la lista hacia adelante
    def adelante(self):
        actual = self.cabeza
        i = 0
        while actual and i < self.cont:
            print(actual.dato)
            actual = actual.siguiente
            i += 1

    # Metodo para recorrer la lista hacia atras
    def atras(self):
        actual = self.cola
        i = 0
        while actual and i < self.cont:
            print(actual.dato)
            actual = actual.anterior
            i += 1


# Probamos la lista agregando algunos datos
l1 = ListaDoble()
l1.agregar(456)
l1.agregar(444)
l1.agregar(555)
l1.agregar(678)

# Imprimimos la lista de cabeza a cola
l1.adelante()
print("="*50)
# Imprimimos la lista de cola a cabeza
l1.atras()
