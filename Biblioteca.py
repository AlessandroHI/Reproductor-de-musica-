from typing import List
from Lista import Lista

class Biblioteca(Lista):

    def __init__(self,artista,album,cancion,imagen,ruta):
        self.artista = artista
        self.album = album
        self.cancion = cancion
        self.imagen = imagen
        self.ruta =ruta
        super().__init__()