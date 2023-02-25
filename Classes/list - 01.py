num = [2, 3, 7, 8]
num[2] = 5
#append vai adicionar o valor 7 no final da lista
num.append(7)
#sort vai ordenar a lista ou também pode ser colocado como reverse para colocar de trás pra frente
num.sort(reverse=True)
#insert vai inserir o valor 0 na posição 2
num.insert(2, 0)
#remove eliminar a primeira ocorrencia da lista caso tenha o 2 repetido
num.remove(2)
#pop elimina o valor 3 da lista
num.pop(3)

print(num)
print(f'Essa lista tem {len(num)} elementos')

#----------------------
valores = [] #lista vazia ou valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei no final da lista')

#----------------------------

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(a)
print(b)

