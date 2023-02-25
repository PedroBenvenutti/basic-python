numero = int(input('Qual numero você deseja a tabuada?: '))

print(f'A tabuada de {numero} é:')
for c in range(1, 11):
    print(f'{numero} x {c} = {c * numero}')