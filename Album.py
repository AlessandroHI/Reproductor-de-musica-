from Lista import Lista

class Album(Lista):

    def __init__(self,nombre):
        self.nombre = nombre
        super().__init__()
