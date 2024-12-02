'''
Created on 9 nov 2024

@author: vidal
'''
from entrega2.tipos2.Cola import Cola

print("TEST DE COLA:")
print("#")

cola = Cola.of()
cola.add_all([23, 47, 1, 2, -3, 4, 5])
print("Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5")
print("Resultado de la cola:", cola)

print("#" * 48)
print("Elementos eliminados utilizando remove_all:", cola.remove_all())

