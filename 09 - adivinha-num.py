import random

lista = [0, 1, 2, 3, 4, 5]
random.choice(lista)

advinha = int(input("Tente adivinhar o numero de 0 a 5! Insira aqui: "))

if advinha == random.choice(lista):
    print(f'Você acertou!')
else:
    print(f'Você errou. O número era {random.choice(lista)} ')


