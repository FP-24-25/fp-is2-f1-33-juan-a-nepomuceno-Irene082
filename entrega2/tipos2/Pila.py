'''
Created on 9 nov 2024

@author: vidal
'''
from entrega2.tipos2.Agregado_lineal import Agregado_lineal

class Pila(Agregado_lineal):
    @staticmethod
    def of() -> 'Pila':
        return Pila()
    
    def add(self, e) -> None:
        self._elements.insert(0, e)
    
    def __str__(self):
        return "Pila(" + ", ".join(map(str, self._elements)) + ")"
