################
# Mariela Carriqueo - @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def codificado(texto, valor_rot):
    """
    Esta función codifica un texto con el método ROT13
    """
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    codificacion = ''
    largo_alfabeto = len(alfabeto)
    for letra in texto:
        valor_letra = ord(letra)
        rotacion = (valor_letra - 65 + valor_rot) % largo_alfabeto
        codificacion += alfabeto[rotacion]
    return codificacion

def decodificado(texto, valor_rot):
    """
    Esta función decodifica un texto con el método ROT13
    """
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decodificacion = ''
    largo_alfabeto = len(alfabeto)
    for letra in texto:
        valor_letra = ord(letra)
        rotacion = (valor_letra - 65 + valor_rot) % largo_alfabeto
        decodificacion += alfabeto[rotacion]
    return decodificacion

def prueba():
    texto = input('Ingrese texto: ')
    valor_rot = int(input('Ingrese valor de rotación: '))
    valor = decodificado(texto, valor_rot)
    print(f'{valor}')
    

if __name__ == "__main__":
    prueba()
   
            
            
        



    