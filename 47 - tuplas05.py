listagem = ('Pão', 1, 'Leite', 3.50, 'Açucar', 8, 'Feijão', 8.75, 'Arroz', 10.50, 'Margarina', 5.50)

print('-' * 30)
print('      LISTAGEM DE PREÇOS')
print('-' * 30)
cont = 0
preco = 1

for c in listagem:
    print(f'{listagem[cont]:.<30}{listagem[cont + 1]:.2f}')
    cont += 2
    preco += 1
