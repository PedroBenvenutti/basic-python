def moeda(f):
    return f'R${f:.2f}'


def aumentar(n, formatado=False):
    if formatado == True:
        return moeda(n * 1.8)
    return n * 1.8


def diminuir(n, formatado=False):
    if formatado == True:
        return moeda(n * 0.65)
    return n * 0.65


def dobro(n, formatado=False):
    if formatado == True:
        return moeda(n * 2)
    return n * 2


def metade(n, formatado=False):
    if formatado == True:
        return moeda(n / 2)
    return n / 2



