'''
Created on 9 nov 2024

@author: vidal
'''
from entrega2.tipos2.Lista_ordenada import Lista_ordenada

print("TEST DE LISTA ORDENADA:")
print("#")

# Creación de una lista con criterio de orden lambda x: x
lista = Lista_ordenada.of(lambda x: x)
lista.add(3)
lista.add(1)
lista.add(2)
print("Creación de una lista con criterio de orden lambda x: x")
print("Se añade en este orden: 3, 1, 2")
print("Resultado de la lista:", lista)

print("#")
print("El elemento eliminado al utilizar remove():", lista.remove())

print("#")
lista.add_all([1, 2, 3])
print("Elementos eliminados utilizando remove_all:", lista.remove_all())

print("#")
print("Comprobando si se añaden los números en la posición correcta...")
lista.add_all([1, 2, 3])
lista.add(0)
print("Lista después de añadirle el 0:", lista)
lista.add(10)
print("Lista después de añadirle el 10:", lista)
lista.add(7)
print("Lista después de añadirle el 7:", lista)
