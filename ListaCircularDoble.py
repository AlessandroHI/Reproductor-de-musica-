from Nodo import Nodo

class LIstacircular:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.contador = 0

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos()

    def agregar(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__unir_nodos()
        self.contador +=0
        
    def __unir_nodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero
   
    def recorrer_inicio(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def len(self):
        return self.contador
            
        