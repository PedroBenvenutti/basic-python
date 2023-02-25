from ex107 import moeda

p = float(input(f'Digite o preço: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 80% de {moeda.moeda(p)} é {moeda.aumentar(p, True)}')
print(f'Reduzindo 35% de {moeda.moeda(p)} é {moeda.diminuir(p, True)}')