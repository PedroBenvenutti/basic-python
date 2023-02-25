dados = {}
lista = []
cont = media = soma = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite um sexo válido.')
    dados['idade'] = float(input('Idade: '))
    cont += 1
    soma += dados['idade']
    media = soma / cont
    lista.append(dados.copy())
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A média de idade do grupo é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print(f'\nLista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRADO >>')







