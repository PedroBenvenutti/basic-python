nome = str(input('Qual seu nome? '))
if nome == 'Pedro':
    print(f'Que nome bonito! {nome}')
print(f'Bom dia, {nome}')
print('===================')

n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))
m = (n1+n2)/2

print(f'Sua média foi de {m}')
if m >= 7:
    print(f'Parabéns {nome}, Você passou de ano!')
else:
    print(f'Você está em recuperação {nome}.')

