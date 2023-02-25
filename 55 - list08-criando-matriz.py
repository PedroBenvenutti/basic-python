linha1 = []
linha2 = []
linha3 = []
matriz = [linha1, linha2, linha3]

for i in range(0, 3):
    n = int(input(f'Digite o numero para a posição [0, {i}]'))
    linha1.append(n)
for i in range(0, 3):
    n = int(input(f'Digite o numero para a posição [1, {i}]'))
    linha2.append(n)
for i in range(0, 3):
    n = int(input(f'Digite o numero para a posição [2, {i}]'))
    linha3.append(n)
print(f'[ {matriz[0][0]} ]', end='')
print(f'[ {matriz[0][1]} ]', end='')
print(f'[ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ]', end='')
print(f'[ {matriz[1][1]} ]', end='')
print(f'[ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ]', end='')
print(f'[ {matriz[2][1]} ]', end='')
print(f'[ {matriz[2][2]} ]')

#####SOLUÇÃO OTIMIZADA

matriz2 = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz2[l][c] = int(input(f'Digite um valor para [{l} e {c}]: '))
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz2[l][c]}', end='')
    print()