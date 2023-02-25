num = []
continuar = ''

while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
    else:
        print('Valor repetido')
    continuar = str(input('Deseja continuar? [S] [N]')).strip().upper()
    while continuar not in 'SsNn':
        print('Digite apenas valores válidos.')
        continuar = str(input('Deseja continuar? [S] [N]')).strip().upper()

    if continuar == 'N':
        break
print(sorted(num))