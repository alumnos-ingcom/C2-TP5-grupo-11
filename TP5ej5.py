################
# Mariela Carriqueo - @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def inversion_de_mayuscula(texto):
    """
    Esta función convierte revierte las mayúsculas en minúsculas y viceversa.
    """
    txt  = str.swapcase(texto)
    return txt

def prueba():
    texto = input('Ingrese texto: ')
    valor = inversion_de_mayuscula(texto)
    print(f'{valor}')
    

if __name__ == "__main__":
    prueba()
   
            
            
        