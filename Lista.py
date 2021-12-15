
from Nodo import Nodo

class Lista(Nodo):
    def __init__(self):
        super().__init__()
        self.cabeza = Nodo()
        self.contador = 0
        
    def append(self, nuevo_nodo):
        nodo = self.cabeza
        while(nodo.siguiente):
            nodo = nodo.siguiente
        nodo.siguiente = nuevo_nodo
        self.contador += 1
        

    def get(self, i):
        if (i >= self.contador):
            return None
        nodo = self.cabeza.siguiente
        n = 0
        while(nodo):
            if (n == i):
                return nodo
            nodo = nodo.siguiente
            n += 1

    def __getitem__(self, i):
        return self.get(i)

    def len(self):
        return self.contador

        
