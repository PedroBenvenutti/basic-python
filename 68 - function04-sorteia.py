from random import randint

numeros = list()


def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Os numeros sorteados foram {lista}.')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares da {lista} é {soma}.')


sorteia(numeros)
somaPar(numeros)

