soma = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = c + soma
print(f'A soma de todos os números divisíveis por 3 no intervalor 1 a 500 é de {soma}.')
