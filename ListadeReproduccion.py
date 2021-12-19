from Lista import Lista

class Reproducciones(Lista):

    def __init__(self,cancion,album,artista,cont):
        self.cancion = cancion
        self.album = album
        self.artista = artista
        self.cont = cont
        super().__init__()