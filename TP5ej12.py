################
# Mariela Carriqueo - @MCarriqueo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def comparar_listas(lista1, lista2):
    """
    Esta función indica True si dos listas contienen los mismos elementos.
    """
    comparacion = []
    for valor in lista1:
        if valor in lista2:
            return True
        else:
            False
        
def prueba():
    lista1=[]
    for i in range(3):
        dato = input('Ingrese valor: ')
        lista1.append(dato)
    lista2=[]
    for i in range(3):
        dat = input('Ingrese valor: ')
        lista2.append(dat)
    respuesta= comparar_listas(lista1,lista2)
    print(f'{respuesta}')
    
    

if __name__ == "__main__":
    prueba()
   
            
            
        



    