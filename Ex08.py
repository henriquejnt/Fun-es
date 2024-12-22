"""Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres 
embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer 
outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos
 em caixa alta ou caixa baixa, independentemente de como foram digitados."""

from random import shuffle
def embaralha_string(string):
    embaralha = list(string)
    shuffle(embaralha)
    return ''.join(embaralha)


frase = input('Digite uma paravra ou frase: ')
resultado = embaralha_string(string=frase)
print("String normal: ", frase.lower())
print("String embaralhada: ", resultado.lower())