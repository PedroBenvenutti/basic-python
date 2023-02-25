numero = int(input('\033[4;31mInsira um número inteiro:\033[m '))


op = int(input('Pressione \033[31m1\033[m para converter para \033[31mbinário\033[m.\nPressione \033[31m2\033[m para converter para \033[31moctal\033[m.\nPressione \033[31m3\033[m para converter para \033[31mhexadecimal\033[m\nOpção: '))

if op == 1:
    print(f'O número em binário é: {bin(numero)}')
elif op == 2:
    print(f'O número em octal é: {oct(numero)}')
elif op == 3:
    print(f'O número em hexadecimal é {hex(numero)}')
else:
    print('\033[1:31mOpção não válida!!!\033[m.')