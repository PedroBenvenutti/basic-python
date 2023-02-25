n = cont = 0


while True:
    print('-=' * 10)
    n = int(input('Digite um valor para ver a tabuada (valor negativo para encerrar): '))
    print('-=' * 10)
    if n < 0:
        break
    for cont in range(0, 10, 1):
        cont += 1
        print(f'{n} x {cont} = {n * cont}')

print('FIM!')
