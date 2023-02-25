linha1 = []
linha2 = []
linha3 = []
matriz = [linha1, linha2, linha3]
pares = somacol3 = maior = 0

for i in range(0, 3):
    n = int(input(f'Digite o numero para a posição [0, {i}]'))
    linha1.append(n)
    if n % 2 == 0:
        pares += n
    if i == 2:
        somacol3 += n
for i in range(0, 3):
    n = int(input(f'Digite o numero para a posição [1, {i}]'))
    linha2.append(n)
    if n % 2 == 0:
        pares += n
    if i == 2:
        somacol3 += n
    if len(linha2) == 0:
        maior = linha2[0]
    else:
        if linha2[i] > maior:
            maior = linha2[i]

for i in range(0, 3):
    n = int(input(f'Digite o numero para a posição [2, {i}]'))
    linha3.append(n)
    if n % 2 == 0:
        pares += n
    if i == 2:
        somacol3 += n



print(f'[ {matriz[0][0]} ]', end='')
print(f'[ {matriz[0][1]} ]', end='')
print(f'[ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ]', end='')
print(f'[ {matriz[1][1]} ]', end='')
print(f'[ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ]', end='')
print(f'[ {matriz[2][1]} ]', end='')
print(f'[ {matriz[2][2]} ]')
print(f'=-'*20)

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {somacol3}.')
print(f'O maior valor da segunda linha é {maior}')
