#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
# se seu argumento for positivo, e ‘N’, 
# se seu argumento for zero ou negativo.
def verde_falso(num: int):
    if num >0:
        return print('P')
    else:
        return  print('N')
    
verde_falso(num=-2)