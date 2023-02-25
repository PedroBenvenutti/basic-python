frase = str(input('Digite uma frase: ').strip().upper().replace(" ", ""))

inverso = ''

for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
if inverso == frase:
    print(f'{frase} é um Palíndromo.')
else:
    print('A frase digitada não é um Palíndromo')

