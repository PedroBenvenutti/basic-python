from time import sleep


def maior(*num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 9, 5, 7, 3, 5)
maior(4, 7, 8)
maior(3, 8)
maior(6)
maior(int(input("N: ")))
