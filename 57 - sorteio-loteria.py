from random import sample
from time import sleep
njogos = int(input('Quantos jogos você quer sortear?: '))
jogo = list()
palpites = list()
print('-='*5)
print(f'SORTEANDO {njogos} JOGOS')
print('-='*5)
for n in range(0, njogos):
    jogo = sample(range(1, 61), 6)
    jogo.sort()
    palpites.append(jogo[:])
    print(f'Jogo {n+1}: {palpites[n]}')
    sleep(1)
print('-='*5, end='')
print('BOA SORTE', end='')
print('-='*5)