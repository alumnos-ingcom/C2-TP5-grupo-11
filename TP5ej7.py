################
# Mariela Carriqueo - @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def distancia(num1, num2):
    """
    Esta función determina la distancia entre dos números
    """
    d = num2 - num1
    if d < 0:
        d= d * -1
    return d


def prueba():
    num1 = float(input('Ingrese primer valor: '))
    num2 = float(input('Ingrese segundo valor: '))
    valor = distancia(num1,num2)
    print(f'La distancia entre ambos valores es: {valor}')
    

if __name__ == "__main__":
    prueba()
   
            
            
        