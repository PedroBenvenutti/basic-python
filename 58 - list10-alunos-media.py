cadastro = []
geral = []
continuar = ''
med = notas = 0
cabeçalho = ['No.', 'NOME', 'MÉDIA']

while True:
    cadastro.append(str(input('Aluno: ')))
    cadastro.append(float(input('Nota 1: ')))
    cadastro.append((float(input('Nota 2: '))))
    cadastro.append((cadastro[1] + cadastro[2]) / 2)
    geral.append(cadastro[:])
    cadastro.clear()
    continuar = str(input('Deseja continuar? [S] [N]')).strip().upper()
    while continuar not in 'SNsn':
        continuar = str(input('Deseja continuar? [S] [N]')).strip().upper()
    if continuar == 'N':
        break
print('-='*15)
print(f'{cabeçalho[0]:<3} {cabeçalho[1]:<7} {cabeçalho[2]:>5}')
print('-'*30)
for l in range(0, len(geral)):
    print(f'{l:<3} {geral[l][0]:<7} {geral[l][3]:>5}')
print('-'*30)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    for n in range(0, len(geral)):
        if notas == n:
            print(f'Notas de {geral[n][0]} são {geral[n][1]} e {geral[n][2]}.')
    if notas == 999:
        print('Obrigado, volte sempre.')
        break