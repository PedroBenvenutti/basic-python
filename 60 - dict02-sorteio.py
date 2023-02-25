from random import randint
from time import sleep
dados = {}
dados['Jogador1'] = randint(1, 6)
dados['Jogador2'] = randint(1, 6)
dados['Jogador3'] = randint(1, 6)
dados['Jogador4'] = randint(1, 6)
cont = 1

print("Valores sorteados:")
for k, v in dados.items():
    print(f'O {k} tirou {v}.')
    sleep(1)
print('Ranking dos jogadores: ')

for i in sorted(dados, key=dados.get, reverse=True):
    print(f'{cont}º lugar: {i} com {dados[i]}')
    cont += 1