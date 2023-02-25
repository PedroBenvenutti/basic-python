from random import randint


tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os numeros sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {sorted(tupla)[-1]}')
print(f'O menor valor sorteado foi {sorted(tupla)[0]}')
