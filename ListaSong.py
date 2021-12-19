from typing import List
from Lista import Lista

class ListaSong(Lista):

    def __init__(self,artista,album):
        self.artista = artista
        self.album = album
        super().__init__()