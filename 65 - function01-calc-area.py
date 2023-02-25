print('Controle de terrenos')
print('-'*20)


def area(l, c):
    a = l * c
    print(f'A área do terreno {l}x{c} é de {a}m2.')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)


