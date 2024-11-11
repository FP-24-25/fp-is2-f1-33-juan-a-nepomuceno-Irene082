'''
Created on 9 nov 2024

@author: vidal
'''
from typing import Callable, TypeVar, Generic
from entrega2.tipos2.Agregado_lineal import Agregado_lineal


E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada_sin_repeticion(Agregado_lineal, Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order
    
    @staticmethod
    def of(order: Callable[[E], R]) -> 'Lista_ordenada_sin_repeticion':
        return Lista_ordenada_sin_repeticion(order)
    
    def __index_order(self, e: E) -> int:
        for i, element in enumerate(self._elements):
            if self._order(e) <= self._order(element):
                return i
        return len(self._elements)
    
    def add(self, e: E) -> None:
        if e not in self._elements:
            index = self.__index_order(e)
            self._elements.insert(index, e)
    
    def __str__(self):
        return "ListaOrdenadaSinRepeticion(" + ", ".join(map(str, self._elements)) + ")"
