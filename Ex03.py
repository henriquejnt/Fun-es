#Faça um programa, com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.
def somatorio(n1,n2,n3: float):
    return n1+n2+n2

n1 = float(input('Valor 1: '))
n2 = float(input('Valor 2: '))
n3 = float(input('Valor 3: '))
soma = somatorio(n1,n2,n3)
print(soma)