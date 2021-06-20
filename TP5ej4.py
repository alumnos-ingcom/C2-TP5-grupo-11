################
# Mariela Carriqueo - @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP5ej1 import ingreso_entero
def es_perfecto(numero):
    """
    Esta función determina si un número entero positivo es perfecto.
    """
    suma = 0
    
    for i in range(numero-1):
        if  numero % (i + 1) == 0 and i < numero: 
            suma += i + 1
    if suma == numero:
        return True
    else:
        return False
           
   
def prueba():
    num = ingreso_entero('Ingrese un número entero')
    valor = es_perfecto(num)
    print(f' el numero es {valor}' )
    

if __name__ == "__main__":
    prueba()
   
            
            
        