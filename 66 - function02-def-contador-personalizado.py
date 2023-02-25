from time import sleep

def contador(a, b, c):
    print('-=' * 20)
    print(f'Contagem de 1 até 10 de 1 em 1')
    for i in range(1, 11, 1):
        sleep(0.5)
        print(f'{i} ', end="")
    print('FIM!')
    print('-=' * 20)
    print(f'Contagem de 10 até 0 de 2 em 2')
    for f in range(10, -1, -2):
        sleep(0.5)
        print(f'{f} ', end="")
    print('FIM!')
    print('Agora é sua vez de personalizar a contagem!')
    if c == 0:
        c = 1
    if a > b:
        c = c * -1
    for p in range(a, b, c):
        sleep(0.5)
        print(f'{p} ', end="")
    print(f'{b} ', end="")
    print('FIM!')


contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))