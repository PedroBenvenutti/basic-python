time = list()
dados = {}
gols = []
soma = 0
npartidas = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    npartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gols.clear()
    for c in range(0, npartidas):
        ngols = int(input(f'Quantos gols {dados["nome"]} marcou na partida {c+1}?'))
        soma += ngols
        gols.append(ngols)
    dados['total'] = soma
    dados['gols'] = gols
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar?: [S] [N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? 999 para finalizar: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe Jogador com código {busca}')
    else:
        print(f'-- Levantamento do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No  {i+1} fez {g} gols.')
    print('-' *40)
print('VOLTE SEMPRE')




