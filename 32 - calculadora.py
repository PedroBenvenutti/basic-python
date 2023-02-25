print('\033[031m=-=-=CALCULADORA=-=-=')
valor1 = int(input('Insira o primeiro número: '))
valor2 = int(input('Insira o segundo número: \033[m'))
opcao = int(input('MENU\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR NÚMERO\n[4] INSERIR NOVOS NÚMEROS\n[5] FECHAR PROGRAMA\n'))

while opcao != 5:
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é {soma}.')
        print('\033[031m=-=-=CALCULADORA=-=-=\033[m')
        opcao = int(input('MENU\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR NÚMERO\n[4] INSERIR NOVOS NÚMEROS\n[5] FECHAR PROGRAMA\n'))
    if opcao == 2:
        mult = valor1 * valor2
        print(f'A multiplicação entre {valor1} e {valor2} é {mult}.')
        print('\033[031m=-=-=CALCULADORA=-=-=\033[m')
        opcao = int(input('MENU\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR NÚMERO\n[4] INSERIR NOVOS NÚMEROS\n[5] FECHAR PROGRAMA\n'))
    if opcao == 3:
        maior = 0
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'O maior valor entre {valor1} e {valor2} é {maior}.')
        print('\033[031m=-=-=CALCULADORA=-=-=\033[m')
        opcao = int(input('MENU\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR NÚMERO\n[4] INSERIR NOVOS NÚMEROS\n[5] FECHAR PROGRAMA\n'))
    if opcao == 4:
        valor1 = int(input('\033[031mInsira o primeiro número: '))
        valor2 = int(input('Insira o segundo número: \033[m'))
        opcao = int(input('MENU\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR NÚMERO\n[4] INSERIR NOVOS NÚMEROS\n[5] FECHAR PROGRAMA\n'))
print('Obrigado por usar Pedrolator!')
print('O PROGRAMA FOI FINALIZADO')

