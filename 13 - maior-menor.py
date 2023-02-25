n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))
n3 = float(input('Insira o terceiro numero: '))
#Verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'\033[1;31mO maior número é {maior}\033[m')

#Verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'\033[1;32mO menor número é {menor}\033[m')