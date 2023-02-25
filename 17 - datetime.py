from datetime import date

hoje = date.today().year

ano = int(input('Informe seu ano de nascimento: '))

idade = hoje - ano
print(f'Você está com {idade} anos.')

if idade < 18:
    print(f'Ainda não está na hora de você se alistar. Ainda faltam {18 - idade} anos para o alistamento.')
elif idade == 18:
    print('Já está na hora de você se alistar.')
else:
    print(f'Seu prazo de alistamento ja passou fazem {idade - 18} anos, favor se apresentar o mais rápido possível.')