'''
Created on 9 nov 2024

@author: vidal
'''
from entrega2.tipos2.Lista_ordenada_sin_repeticiones import Lista_ordenada_sin_repeticion

# Resto del código de pruebas...

print("TEST DE LISTA ORDENADA SIN REPETICIÓN:")
print("#")

# Creación de una lista con criterio de orden lambda x: -x
lista_sin_repe = Lista_ordenada_sin_repeticion.of(lambda x: -x)
lista_sin_repe.add_all([23, 47, 47, 1, 2, -3, 4, 5])
print("Creación de una lista con criterio de orden lambda x: -x")
print("Se añade en este orden: 23, 47, 47, 1, 2, -3, 4, 5")
print("Resultado de la lista ordenada sin repetición:", lista_sin_repe)

print("#")
print("El elemento eliminado al utilizar remove():", lista_sin_repe.remove())

print("#")
print("Elementos eliminados utilizando remove_all:", lista_sin_repe.remove_all())

print("#")
print("Comprobando si se añaden los números en la posición correcta...")
lista_sin_repe.add_all([47, 23, 5, 4, 2, 1, -3])
lista_sin_repe.add(0)
print("Lista después de añadirle el 0:", lista_sin_repe)
lista_sin_repe.add(0)
print("Lista después de añadirle el 0:", lista_sin_repe)
lista_sin_repe.add(7)
print("Lista después de añadirle el 7:", lista_sin_repe)
