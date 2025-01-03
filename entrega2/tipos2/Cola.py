'''
Created on 9 nov 2024

@author: vidal
'''
from entrega2.tipos2.Agregado_lineal import Agregado_lineal

class Cola(Agregado_lineal):
    @staticmethod
    def of() -> 'Cola':
        return Cola()
    
    def add(self, e) -> None:
        self._elements.append(e)
    
    def __str__(self):
        return "Cola(" + ", ".join(map(str, self._elements)) + ")"
