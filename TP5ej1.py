################
# Mariela Carriqueo - @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingreso_entero(mensaje):
    """
    Esta función muestra un mensaje y agrega # para indicar el ingreso de un número entero.
    """
    ingreso = input(mensaje + "  #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero
       
class IngresoIncorrecto(Exception):
    """Esta es la excepcion para el ingreso incorrecto de un número"""
    pass

def es_par(numero):
    """
    Esta función indica si un número es par o impar.
    """
    divisor = 2
    resultado = int(numero / divisor)
    resto = numero - resultado * divisor
    if resto == 0:
        return True
    else:
        return False
    
def prueba():
    num = ingreso_entero('Ingrese un número entero')
    valor = es_par(num)
    print(f'{valor}' )
    

if __name__ == "__main__":
    prueba()

    