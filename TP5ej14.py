################
# Mariela Carriqueo - @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_capicua(numero):
    """
    Esta función determina si un número entero positivo es capicúa.
    """
    num_inv = numero[::-1]
    if numero == num_inv:
        return True
  

def prueba():
    num = input('Ingrese un valor: ')
    valor = es_capicua(num)
    if valor == True:
        print(f'El número es capicúa')
    else:
        print(f'El número no es capicúa')
    

if __name__ == "__main__":
    prueba()
    
        