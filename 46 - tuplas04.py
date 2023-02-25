tupla = (int(input('Insira o primeiro valor: ')),
int(input('Insira o segundo valor: ')),
int(input('Insira o terceiro valor: ')),
int(input('Insira o último valor: ')))

print(f'O número 9 apareceu {tupla.count(9)} vezes.')

if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3)+1}ª posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print(f'Os números pares digitados foram: ', end="")
for num in tupla:
    if num % 2 == 0:
        print(num,"", end="")

