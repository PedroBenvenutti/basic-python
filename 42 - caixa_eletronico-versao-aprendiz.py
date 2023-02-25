print('-=' * 10)
print('\033[4;031mCAIXA ELETRÔNICO\033[m')
print('-=' * 10)
ced50 = ced20 = ced10 = ced01 = mod50 = mod20 = mod10 = mod01 = 1
transacao = ''



while True:
    print('\033[036m-=\033[m' *20)
    valor = int(input('Bom dia, informe o valor do saque: R$'))

#Quando o valor solicitado for maior que 50
    if valor >= 50:
        ced50 = valor // 50
        mod50 = valor % 50
        if mod50 == 0:
            print(f'Você recebeu {ced50} nota(s) de R$50.')
        elif mod50 > 20:
            ced20 = mod50 // 20
            mod20 = mod50 % 20
            if mod20 == 0:
                print(f'Você recebeu {ced50} nota(s) de R$50, {ced20} nota(s) de R$20.')
            elif mod20 >= 10:
                ced10 = mod20 // 10
                mod10 = mod20 % 10
                if mod10 == 0:
                    print(f'Você recebeu {ced50} nota(s) de R$50, {ced20} nota(s) de R$20 e {ced10} nota(s) de R$10.')
                elif mod10 < 10:
                    ced01 = mod10 // 1
                    mod01 = mod10 % 1
                    print(f'Você recebeu {ced50} nota(s) de R$50, {ced20} nota(s) de R$20, {ced10} nota(s) de R$10 e {ced01} nota(s) de R$1.')
            elif mod20 < 10:
                ced01 = mod20 // 1
                mod01 = mod20 % 1
                print(f'Você recebeu {ced50} nota(s) de R$50, {ced20} nota(s) de R$20 e {ced01} nota(s) de R$1.')
        elif (mod50 < 20) and (mod50 >= 10):
            ced10 = mod50 // 10
            mod10 = mod50 % 10
            if mod10 == 0:
                print(f'Você recebeu {ced50} nota(s) de R$50 e {ced10} nota(s) de R$10.')
            elif mod10 < 10:
                ced01 = mod10 // 1
                mod01 = mod10 % 1
                if mod01 ==0:
                    print(f'Você recebeu {ced50} nota(s) de R$50, {ced10} nota(s) de R$10 e {ced01} nota(s) de R$1.')
            else:
                ced01 = mod10 // 1
                mod01 = mod10 % 1
                print(f'Você recebeu {ced50} nota(s) de R$50 e {ced01} nota(s) de R$1')
        elif mod50 < 10:
            ced01 = mod50 // 1
            mod01 = mod50 % 1
            print(f'Você recebeu {ced50} nota(s) de R$50 e {ced01} nota(s) de R$1.')

#Quando o valor solicitado estiver entre 49 e 20
    if (valor < 50) and (valor >= 20):
        ced20 = valor // 20
        mod20 = valor % 20
        if mod20 == 0:
            print(f'Você recebeu {ced20} nota(s) de R$20.')
        if mod20 > 10:
            ced10 = mod20 // 10
            mod10 = mod20 % 10
            if mod10 == 0:
                print(f'Você recebeu {ced20} nota(s) de R$20 e {ced10} nota(s) de R$10.')
            else:
                ced01 = mod10 // 1
                mod01 = mod10 % 1
                if mod01 == 0:
                    print(f'Você recebeu {ced20} nota(s) de R$20, {ced10} nota(s) de R$10 e {ced01} nota(s) de R$1.')
        if (mod20 < 10) and (mod20 > 0):
            ced01 = mod20 // 1
            mod01 = mod20 % 1
            if mod01 == 0:
                print(f'Você recebeu {ced20} nota(s) de R$20 e {ced01} nota(s) de R$1.')

#Quando o valor for menor que 19
    if (valor < 20) and (valor > 10):
        ced10 = valor // 10
        mod10 = valor % 10
        if mod10 == 0:
            print(f'Você recebeu {ced10} nota(s) de R$10.')
        else:
            ced01 = mod10 // 1
            mod01 = mod10 % 1
            if mod01 == 0:
                print(f'Você recebeu {ced10} nota(s) de R$10 e {ced01} nota(s) de R$1.')

#Valor mínimo para saque é de R$10
    if valor < 10:
        print('Valor mínimo de saque é R$10.')

#Deseja continuar? break
    print('\033[036m-=\033[m' *20)
    transacao = (input('Deseja efetuar mais alguma transação? [S] [N]')).upper().strip()[0]
    while transacao != 'S' and transacao != 'N':
        transacao = (input('Deseja efetuar mais alguma transação? APENAS [S] ou [N]')).upper().strip()[0]
    if transacao == 'N':
        break


print("\nObrigado por usar Benvenutti's bank!")
print('Volte sempre.')


