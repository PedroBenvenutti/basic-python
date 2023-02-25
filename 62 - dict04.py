dados = {}
gols = []
soma = 0
npartidas = 0

dados['nome'] = str(input('Nome do jogador: '))
npartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, npartidas):
    ngols = int(input(f'Quantos gols {dados["nome"]} marcou na partida {c+1}?'))
    soma += ngols
    gols.append(ngols)
dados['total'] = soma
dados['gols'] = gols

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*15)
print(f'O jogador {dados["nome"]} jogou {npartidas} partidas.')
for k, v in enumerate(dados['gols']):
    print(f'=> Na partida {k+1}, fez {v} gols.')
print(f'Total de {dados["total"]} gols.')