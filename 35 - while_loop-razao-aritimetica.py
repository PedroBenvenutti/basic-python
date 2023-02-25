print('\033[1:31mGerador de PA\033[m')
print('-=' * 10)
numero = int(input('Insira o numero: '))
razao = int(input('Insira a razão aritimética: '))
termo = numero
cont = 1
add = 10
total = 0
while add != 0:
    total = total + add
    while cont <= total:
        print(f'{termo} -> ', end="")
        termo += razao
        cont += 1
    print('Pausa')
    add = int(input('\nGostaria de adicionar mais termos?\nDigite a quantidade ou pressione "0" para encerrar: '))
print('Fim.')