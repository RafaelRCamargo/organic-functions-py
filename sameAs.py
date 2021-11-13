# Os
import os

arr = []
msg = ""

class SameAs:
    def __init__(self, name):
        arr.append([name, 0])
        qtd = 0

    def addOn(self, name):
        for x in arr:
            if(x[0] == name):
                x[1] += 1

    def toString(self):
        listToStr = ' '
        elem = ''
        for elem in arr:
            for x in elem:
                listToStr += f" {x}"
        return listToStr

    def clear(self):
        arr.clear()
