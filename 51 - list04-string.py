lista = []

while True:
    n = int(input('Insira um número: '))
    lista.append(n)
    continuar = str(input('Deseja continuar? [S] [N]')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S] [N]')).strip().upper()
    if continuar == 'N':
        break


print(f'Foram digitados um total de {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é {lista}')
if 5 in lista:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')


