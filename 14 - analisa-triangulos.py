print('\033[31;40m-=\033[m'*20)
print('\033[1;33;46mAnalisador de triangulos\033[m')
print('\033[31;40m-=\033[m'*20)
r1 = int(input('Insira a medida da primeira reta: '))
r2 = int(input('Insira a medida da segunda reta: '))
r3 = int(input('Insira a medida da terceira reta: '))

lado1 = r1 + r2
lado2 = r1 + r3
lado3 = r2 + r3

if r1 >= lado3:
    print('\033[31mNão podemos fazer um triangulo.\033[m')
if r2 >= lado2:
    print('\033[31mNão podemos fazer um triangulo.\033[m')
if r3 >= lado1:
    print('\033[31mNão podemos fazer um triangulo.\033[m')
else:
    print('\033[32mPodemos fazer um triângulo\033[m')