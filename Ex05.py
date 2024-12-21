#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de 
# uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar
#  estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao
#  programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa
#  deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero
#  para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a
#  quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte
#  forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa,
#  mais 0,1% de juros por dia de atraso.

def valor_pagamento (v1, v2):
        if v2 == 0:
            return (f'Zero dias sem atraso! Pagará apenas a prestação de R${v1} reais!')
        else:
            multa = (3/100)*v1
            juros_dias = ((0.1*v2)/100)*v1
            return (f"""{v2} dias atrasados, com 0,1% de juros por dia de atraso será de R${juros_dias}.
            Terá também 3% de multa devido ao atraso: {multa} 
            Tudo somado: {(juros_dias+multa)+v1}""")
        

while True: 
    valor_prestacao = float(input('Valor da prestação (0 p/ encerrar): '))
    if valor_prestacao == 0:
        break
    dias_atraso = int(input('Número de dias atrasados: '))  
    resultado = valor_pagamento(v1=valor_prestacao, v2=dias_atraso)
    print('=*'*20)
    print('RELATÓRIO DO DIA!')
    print(resultado)
        
