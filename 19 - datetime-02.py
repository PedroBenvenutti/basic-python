from datetime import date
hoje = date.today().year

idade = int(input('Qual seu ano de nascimento?: '))

if hoje - idade <= 9:
    print('Categoria mirim.')
elif hoje - idade > 9 and hoje - idade <= 14:
    print('Categoria infantil.')
elif hoje - idade > 14 and hoje - idade <= 19:
    print('Categoria junior.')
elif hoje - idade > 19 and hoje - idade <= 20:
    print('Categoria senior.')
else:
    print('Categoria master.')