'''
Created on 9 nov 2024

@author: vidal
'''
from entrega2.tipos2.Pila import Pila

def test_pila():
    pila = Pila.of()
    pila.add(1)
    pila.add(2)
    pila.add(3)
    assert str(pila) == "Pila([3, 2, 1])", "La pila no está en el orden correcto."
    
    elemento = pila.remove()
    assert elemento == 3, "El elemento eliminado no es correcto."
    
    todos_los_elementos = pila.remove_all()
    assert todos_los_elementos == [2, 1], "Los elementos eliminados no son correctos."
    
    print("Pruebas de Pila superadas exitosamente.")

if __name__ == '__main__':
    test_pila()
