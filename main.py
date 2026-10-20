from collections import deque

class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        # Tarea 1: Agrega el nodo al final sin perder los anteriores (20 pts)
        nuevo = Nodo(codigo, descripcion)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(f"Código: {actual.codigo} | Descripción: {actual.descripcion}")
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # Tarea 2: Agrega el elemento a la cima (Parte de 15 pts)
        self.items.append(elemento)

    def desapilar(self):
        # Tarea 2: Devuelve y elimina el último elemento; controla pila vacía
        if not self.items:
            print("Advertencia: La pila está vacía.")
            return None
        return self.items.pop()

class ColaOptimizada:
    """
    Reto Individual (15 pts): 
    Usar 'collections.deque' en lugar de una lista estándar con pop(0) 
    optimiza la cola para retirar el elemento más antiguo de forma eficiente (O(1)).
    """
    def __init__(self):
        self.items = deque()

    def encolar(self, elemento):
        # Tarea 3: Agrega el elemento al final (Parte de 15 pts)
        self.items.append(elemento)

    def desencolar(self):
        # Tarea 3 & Reto: Devuelve y elimina el primer elemento (el más antiguo / FIFO)
        if not self.items:
            print("Advertencia: La cola está vacía.")
            return None
        return self.items.popleft()


