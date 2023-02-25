from ex107 import moeda

p = float(input(f'Digite o preço: '))
print(f'A metade de {p} é {moeda.metade(p)}.')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% de {p} é {moeda.aumentar(p)}')
print(f'Reduzindo 13% de {p} é {moeda.diminuir(p)}')