################
# Mariela Carriqueo - @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def codificado(texto):
    """
    Esta función codifica un texto con el método ROT13
    """
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    codificacion = ''
    largo_alfabeto = len(alfabeto)
    for letra in texto:
        valor_letra = ord(letra)
        rotacion = (valor_letra - 65 + 13) % largo_alfabeto
        codificacion += alfabeto[rotacion]
    return codificacion

def decodificado(texto):
    """
    Esta función decodifica un texto con el método ROT13
    """
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decodificacion = ''
    largo_alfabeto = len(alfabeto)
    for letra in texto:
        valor_letra = ord(letra)
        rotacion = (valor_letra - 65 + 13) % largo_alfabeto
        decodificacion += alfabeto[rotacion]
    return decodificacion

def prueba():
    texto = input('Ingrese texto: ')
    valor = decodificado(texto)
    print(f'{valor}')
    

if __name__ == "__main__":
    prueba()
   
            
            
        



    