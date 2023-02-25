nome = str(input('Insira seu nome completo: '))

nomeformatado = nome.strip().title()
lista = nome.title().split()
primeironome = lista[0]
ultimonome = lista[-1]

print(f'O nome completo é {nomeformatado}')
print(f'Seu primeiro nome é {primeironome}')
print(f'O ultimo nome é {ultimonome}')
