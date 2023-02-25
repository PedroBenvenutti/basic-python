valores = []

for c in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {c}: ')))
print(valores)
maior = max(valores)
menor = min(valores)
pos = []
pos2 = []
for c, v in enumerate(valores):
    if maior == v:
        pos.append(c)
    elif menor == v:
        pos2.append(c)
print(f'O maior valor ({maior}) está na posição {pos} e o menor ({menor}) está na posição {pos2}.')









#print(f'O maior valor digitado foi {sorted(valores)[-1]}, na posição {v} ')
#print(f'O menor valor digitado foi {sorted(valores)[0]}, na posição {v}')