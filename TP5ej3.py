################
# Mariela Carriqueo - @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP5ej1 import ingreso_entero

def tribonacci(numero):
    """
    Esta función permite obtener el n-esimo término de la sucesion de Tribonacci.
    """
    n1 = 1
    n2 = 1
    n3 = 1
    for i in range(numero):
        n4 = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = n4
    return n1
    
def prueba():
    num = ingreso_entero('Ingrese un número entero > 3')
    valor = tribonacci(num)
    print(f'{valor}' )
    

if __name__ == "__main__":
    prueba()

    

    