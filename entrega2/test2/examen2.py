'''
Created on 21 nov 2024

@author: vidal
'''
from typing import List, TypeVar, Generic
from entrega2.tipos2.Agregado_lineal import Agregado_lineal

E = TypeVar('E')
P = TypeVar('P')


"EJERCICIO 1"

class ColaConLimite(Agregado_lineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        self.capacidad = capacidad
        self._elements = []  # mete los elementos en una lista vacía

    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError("La cola está llena")
        self._elements.append(e)

    def is_full(self) -> bool:
        return len(self._elements) >= self.capacidad  

    @classmethod
    def of(cls, capacidad: int) -> "ColaConLimite[E]":
        return cls(capacidad)

"EJEMPLO DE USO 1"

cola = ColaConLimite.of(3)
cola.add("Tarea 1")
cola.add("Tarea 2")
cola.add("Tarea 3")
try:
    cola.add("Tarea 4")
except OverflowError as e:
    print(e)
print(cola.remove())











"EJERCICIO 2"

from typing import Callable, Optional, List, TypeVar, Generic


from typing import Callable, Optional, List, TypeVar, Generic

E = TypeVar('E')

class Agregado_lineal(Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0

    @property
    def elements(self) -> List[E]:
        return self._elements

    def add(self, e: E) -> None:
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        if len(self._elements) == 0:
            raise ValueError("El agregado está vacío")
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

    def contains(self, e: E) -> bool:
        return e in self._elements

    def find(self, func: Callable[[E], bool]) -> Optional[E]:
        for element in self._elements:
            if func(element):
                return element
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        return [element for element in self._elements if func(element)]


class AgregadoConcreto(Agregado_lineal[E]):
    def add(self, e: E) -> None:
        self._elements.append(e)







"EJERCICIO 3"

import unittest

class TestAgregadoLineal(unittest.TestCase):
    def setUp(self):
        # Usamos AgregadoConcreto para evitar el NotImplementedError
        self.agregado = AgregadoConcreto[int]()
        self.agregado.add_all([10, 20, 30, 40, 50])

    # Prueba de 'add'
    def test_add(self):
        self.agregado.add(60)
        self.assertIn(60, self.agregado.elements)
    
    # Prueba de 'add_all'
    def test_add_all(self):
        self.agregado.add_all([60, 70])
        self.assertIn(60, self.agregado.elements)
        self.assertIn(70, self.agregado.elements)

    # Prueba de 'remove'
    def test_remove(self):
        removed_element = self.agregado.remove()
        self.assertEqual(removed_element, 10)
        self.assertNotIn(10, self.agregado.elements)

    # Prueba de 'remove_empty' (debe lanzar un error si la lista está vacía)
    def test_remove_empty(self):
        # Vaciar el agregado
        self.agregado.remove_all()
        with self.assertRaises(ValueError):
            self.agregado.remove()

    # Prueba de 'contains'
    def test_contains(self):
        self.assertTrue(self.agregado.contains(30))
        self.assertFalse(self.agregado.contains(100))

    # Prueba de 'find'
    def test_find(self):
        found_element = self.agregado.find(lambda x: x > 25)
        self.assertEqual(found_element, 30)
        self.assertIsNone(self.agregado.find(lambda x: x > 100))

    # Prueba de 'filter'
    def test_filter(self):
        filtered_elements = self.agregado.filter(lambda x: x % 20 == 0)
        self.assertEqual(filtered_elements, [20, 40])

class TestColaConLimite(unittest.TestCase):
    def setUp(self):
        # Configuración de una cola con capacidad 3
        self.cola = ColaConLimite.of(3)

    # Prueba de 'add'
    def test_add(self):
        self.cola.add(10)
        self.cola.add(20)
        self.cola.add(30)
        self.assertEqual(self.cola.elements, [10, 20, 30])

        # Intentar agregar cuando está llena
        with self.assertRaises(OverflowError):
            self.cola.add(40)

    # Prueba de 'remove'
    def test_remove(self):
        self.cola.add(10)
        self.cola.add(20)
        removed_element = self.cola.remove()
        self.assertEqual(removed_element, 10)
        self.assertEqual(self.cola.elements, [20])

    # Prueba de 'remove_empty' (debe lanzar un error si la cola está vacía)
    def test_remove_empty(self):
        with self.assertRaises(ValueError):
            self.cola.remove()

    # Prueba de 'is_full'
    def test_is_full(self):
        self.assertFalse(self.cola.is_full())  # La cola no está llena
        self.cola.add(10)
        self.cola.add(20)
        self.cola.add(30)
        self.assertTrue(self.cola.is_full())  # La cola está llena

if __name__ == "__main__":
    unittest.main()













