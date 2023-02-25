print('-=' *10)

n = 0
cont = 0
soma = n
#ou pode se declarar assim: n = cont = 0

while n != 999:
    n = int(input('Insira um número inteiro: '))
    cont += 1
    soma = soma + n
    if n == 999:
        soma -= 999
print(f'O usuário digitou {cont -1} números.')
print(f'A soma dos números digitados foi de {soma}.')