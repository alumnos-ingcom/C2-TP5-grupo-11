################
# Mariela Carriqueo - @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP5ej1 import ingreso_entero
def fibonacci(numero):
    """
    Esta función permite obtener el n-esimo término de la sucesion de Fibonacci.
    """
    n1 = 0
    n2 = 1
    for i in range(numero):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n1
    
def prueba():
    num = ingreso_entero('Ingrese un número entero > 2')
    valor = fibonacci(num)
    print(f'{valor}' )
    

if __name__ == "__main__":
    prueba()

    

    