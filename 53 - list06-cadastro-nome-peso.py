database = list()
cadastro = list()
maior = menor = 0

while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    if len(database) == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
    database.append(cadastro[:])
    cadastro.clear()
    continuar = str(input('Deseja continuar? [S] [N]')).strip().upper()
    if continuar == 'N':
        break
print('='*30)
print(f'O maior peso foi de {maior}kg. Peso de ', end="")
for p in database:
    if p[1] == maior:
        print(f'{p[0]} ', end="")
print(f'\nO menor peso foi de {menor}kg. ', end="")
for p in database:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print(f'Foram cadastradas {len(data)} pessoas.')

