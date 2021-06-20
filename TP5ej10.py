################
# Mariela Carriqueo - @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_binario(numero):
    """
    Esta función convierte un número entero en binario.
    """
    divisor = 2
    binario = ''
    while numero //2 != 0:
        resto = numero % divisor
        numero = numero // divisor
        binario = str(resto) + binario
    return str(numero) + binario

def convertir_a_entero(binario):
    """
    Esta función convierte un número binario en entero.
    """
    posicion = 0
    numero = 0
    binario = binario[::-1]
    for digito in binario:
        cuenta = 2 ** posicion
        numero += int(digito) * cuenta
        posicion += 1
    return numero

   
def prueba():
    num = str(input('Ingrese un valor: '))
    valor = convertir_a_entero(num)
    print(f'El resultado es: {valor}')
    

if __name__ == "__main__":
    prueba()
   