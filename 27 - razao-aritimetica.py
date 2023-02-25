numero = int(input('Insira o numero: '))
razao = int(input('Insira a razão aritimética: '))
fim = numero + (10-1) * razao

for c in range(numero, fim+1, razao):
    print(c)