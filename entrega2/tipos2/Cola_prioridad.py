'''
Created on 9 nov 2024

@author: vidal
'''
from typing import List, TypeVar, Generic
from entrega2.tipos2.Agregado_lineal import Agregado_lineal

E = TypeVar('E')
P = TypeVar('P')

class ColaPrioridad(Agregado_lineal, Generic[E, P]):
    def __init__(self):
        super().__init__()
        self._priorities: List[P] = []
    
    def add(self, e: E, priority: P) -> None:
        index = self.__index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)
    
    def __index_order(self, priority: P) -> int:
        for i, p in enumerate(self._priorities):
            if priority <= p:
                return i
        return len(self._priorities)
    
    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        self._priorities.pop(0)
        return self._elements.pop(0)
    
    def remove_all(self) -> List[E]:
        removed_elements = self._elements[:]
        self._elements.clear()
        self._priorities.clear()
        return removed_elements
    
    def decrease_priority(self, e: E, new_priority: P) -> None:
        index = self._elements.index(e)
        old_priority = self._priorities[index]
        if new_priority < old_priority:
            self._priorities[index] = new_priority
            self._elements.pop(index)
            self.add(e, new_priority)
    
    def __str__(self):
        return "ColaPrioridad[" + ", ".join([f"({e}, {p})" for e, p in zip(self._elements, self._priorities)]) + "]"
