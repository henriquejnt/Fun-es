#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
#  Por exemplo: 127 -> 721.

def transforma_o_inverso_do_num (inverso):
    div = str(inverso)
    return f"O inverso de {inverso} é {div[::-1]}"

n = int(input("Digite um valor: "))
resultado = transforma_o_inverso_do_num(inverso=n)
print(resultado)

