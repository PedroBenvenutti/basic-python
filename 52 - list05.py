lista = []
pares = []
impar = []

while True:
    n = int(input('Insira um número: '))
    lista.append(n)
    continuar = str(input('Deseja continuar? [S] [N]')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S] [N]')).strip().upper()
    if continuar == 'N':
        break

for pos in range(0, len(lista), 1):
    if lista[pos] % 2 == 0:
        pares.append(lista[pos])
    else:
        impar.append(lista[pos])

print(pares)
print(impar)
print(lista)

