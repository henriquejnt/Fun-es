def triangulo_númerico(n: int):
    lista = []
    lugar = 0
    quantidade_valores = 1
    for valor in range(1, n+1):
        lista.append(valor)
        for localidade in range(quantidade_valores):
            print(lista, end="   ")
        print()
        lugar += 1

triangulo_númerico(10)