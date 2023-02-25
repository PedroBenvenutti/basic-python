n1 = float(input('Qual a primeira nota?: '))
n2 = float(input('Qual a segunda nota?: '))

media = (n1 + n2) / 2

if media < 5:
    print(f'Sua média foi de \033[1:031m{media}\033[m. Você foi reprovado.')
elif media > 5 and media < 6.9:
    print(f'Sua média foi de \033[1:033m{media}\033[m. Você ficou em recuperação.')
else:
    print(f'Sua média foi de \033[1:032m{media}\033[m. Você foi aprovado.')