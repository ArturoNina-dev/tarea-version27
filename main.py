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
        nuevo = Nodo(codigo, descripcion)
        # 1. Agrega el nodo al final sin perder los anteriores
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
            print(f"Código: {actual.codigo}, Descripción: {actual.descripcion}")
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # 2. Agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # 2. Devuelve y elimina el último elemento; controla el caso de pila vacía
        if not self.items:
            return "Error: La pila está vacía"
        return self.items.pop()

class Cola:
    def __init__(self):
        # Reto individual: Usar deque para retirar el elemento más antiguo de manera eficiente O(1)
        self.items = deque()

    def encolar(self, elemento):
        # 3. Agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # 3 y Reto individual: Devuelve y elimina el primer elemento (más antiguo) controlando cola vacía
        if not self.items:
            return "Error: La cola está vacía"
        return self.items.popleft()

# 4. Pruebas con tres elementos
if __name__ == "__main__":
    print("=== 1. PRUEBA DE LISTA ENLAZADA ===")
    lista = ListaEnlazada()
    lista.agregar("E01", "Producto A")
    lista.agregar("E02", "Producto B")
    lista.agregar("E03", "Producto C")
    lista.mostrar()

    print("\n=== 2. PRUEBA DE PILA (LIFO: Last In, First Out) ===")
    pila = Pila()
    pila.apilar("Elemento 1")
    pila.apilar("Elemento 2")
    pila.apilar("Elemento 3")
    print("Desapilado (último agregado):", pila.desapilar())  # Elemento 3
    print("Desapilado (último agregado):", pila.desapilar())  # Elemento 2
    print("Desapilado (último agregado):", pila.desapilar())  # Elemento 1

    print("\n=== 3 Y RETO. PRUEBA DE COLA (FIFO: First In, First Out) ===")
    cola = Cola()
    cola.encolar("Turno 1")
    cola.encolar("Turno 2")
    cola.encolar("Turno 3")
    print("Desencolado (más antiguo):", cola.desencolar())  # Turno 1
    print("Desencolado (más antiguo):", cola.desencolar())  # Turno 2
    print("Desencolado (más antiguo):", cola.desencolar())  # Turno 3

