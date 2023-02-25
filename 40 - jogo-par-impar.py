from random import randint

print('-=' * 20)
print('\033[1;031mJOGO DE PAR OU ÍMPAR\033[m')
print('-=' * 20)
resultado = ""
cont = 0

while True:
    pi = str(input('Você quer par ou ímpar? [P] [I]: ')).upper().strip()
    while (pi != "I") and (pi != "P"):
        print('Você digitou um valor inválido!')
        pi = str(input('Você quer par ou ímpar? [P] [I]: ')).upper().strip()
    if pi == 'P':
        pi = 'PAR'
    if pi == 'I':
        pi = 'IMPAR'
    player = int(input('Selecione um número de 0 a 10: '))
    while player > 10:
        player = int(input('Selecione APENAS números de 0 a 10: '))
    pc = randint(0, 10)
    soma = player + pc
    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "IMPAR"
    if resultado == pi:
        cont += 1
        print(f'\nVocê colocou {player} e o computador colocou {pc}, a soma é {soma}.')
        print(f'Você escolheu {pi} e deu {resultado}.')
    else:
        break

print(f'\nVocê colocou {player} e o computador colocou {pc}, a soma é {soma}.')
print(f'Você escolheu {pi} e deu {resultado}.')
print(f'Você perdeu. A maior sequência de vitórias foi de {cont} vezes.')
if cont >= 5:
    print(f'Mega combo! Mais de {cont} vezes!')

