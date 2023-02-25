nome = str(input('Qual é seu nome?: '))
if nome == 'Pedro':
    print('Que nome bonito!')
elif nome == 'João' or 'Maria' or 'José':
    print('Seu nome é bem popular.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que lindo nome moça.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia \033[1;31m{nome}')
