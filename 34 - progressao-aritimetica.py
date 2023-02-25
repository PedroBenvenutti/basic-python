print('\033[1:31mGerador de PA\033[m')
print('-=' *10)
numero = int(input('Insira o numero: '))
razao = int(input('Insira a razão aritimética: '))
termo = numero
cont = 1


while cont <= 9:
    print(f'{termo} -> ', end="")
    termo = termo + razao
    cont += 1
print(termo)