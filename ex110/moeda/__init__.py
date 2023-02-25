from ex107 import moeda

def resumo(p, aum, desc):
    titulo = 'Resumo do valor'
    print('-'*30)
    print(titulo.center(30, '-'))
    print('-'*30)
    print(f'Preço analisado: \tR${p:.2f}')
    print(f'Dobro do preço: \t{moeda.dobro(p, True)}')
    print(f'Metade do preço: \t{moeda.metade(p, True)}')
    print(f'80% de aumento: \t{moeda.aumentar(p, True)}')
    print(f'35% de desconto: \t{moeda.diminuir(p, True)}')
    print('-' * 30)
    return


