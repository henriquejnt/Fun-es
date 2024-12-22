from random import randint
def jogo_craps ():
    while True:
        dado01 = randint(1,6)
        dado02 = randint(1,6)
        natural = [7,11]
        craps = [2,3,12]
        soma_dados = dado01 + dado02
        if soma_dados in natural:
            print(f'A soma dos dados deu {soma_dados}, é NATURAL, vitória imediata!')
        elif soma_dados in  craps:
            print(f'A soma dos dados deu {soma_dados}, é CRAPS, derrota imediata!')
        else:
            ponto = soma_dados
            print(f'Esse {ponto} número é o ponto do jogador, o jogo continua!')
            while True:
                dado01 = randint(1,6)
                dado02 = randint(1,6)  
                nova_soma = dado01 + dado02
                if nova_soma == ponto:
                    print(f'A soma dos dados deu {nova_soma}, é NATURAL, vitória imediata!')
                    break
                elif nova_soma == 7:
                    print(f'A soma dos dados deu {nova_soma}, é CRAPS, derrota imediata!')
                    break
                else:
                    print('Que sorte, o Ponto apareceu, o jogo continua!')
        s_n = input('Quer continua?[S/N]: ').upper()
        if s_n != 'S':
            break

jogo_craps()