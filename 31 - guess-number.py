from random import randint

comp = randint(0, 10)
guess = int(input('Tente adivinhar o número de 0 a 10: '))
cont = 0
while guess != comp:
    print(f'Você errou, tente novamente.')
    guess = int(input('Tente adivinhar o número de 0 a 10: '))
    cont += 1
print(f'VOCÊ ACERTOU!!! O número é {comp}')
print(f"Você fez {cont} tentativas.")