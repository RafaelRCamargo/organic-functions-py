# Imagehash
from PIL import Image
import imagehash
# Os
import os

class Samples:
    def __init__(self, name):
        self.dirArray = []
        self.itens = 0
        self.name = name
        itens = sum([len(files) for r, d, files in os.walk(('./BancoDeDados/%s' % (self.name)))])
        self.setSamples(itens)

    def setSamples(self, itens):
        i=1
        while i < itens:
            self.dirArray.append(imagehash.average_hash(Image.open(('./BancoDeDados/%s/%d.png' % (self.name, i)))))
            i += 1

    def getItens(self):
        return self.itens

    def getSamples(self):
        return self.dirArray