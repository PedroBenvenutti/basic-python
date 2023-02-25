print('\033[1;032mFATORIAL\033[m')

numero = int(input('Insira um número: '))
n1 = numero
fat = 1

for numero in range(numero, 1, -1):
    print(f'{n1}', end="")
    print(' x ' if n1 > 1 else ' = ', end="")
    fat = fat * n1
    n1 -= 1
print(fat)

