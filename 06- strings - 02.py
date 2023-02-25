nome = str(input('Insira seu nome completo: '))

#maiusculas e minusculas
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

#qual a extensão de nome sem os espaços
nomesemespaços = len(nome)-nome.count(' ')
print(f'A extensão do seu nome sem os espaços é de: {nomesemespaços} letras')

#dividi o nome em uma lista separando os 5 nomes. print lengh da lista na posição 0 que é o primeiro nome
lista = nome.split()
print(f'Seu primeiro nome é {lista[0]} e ele tem {len(lista[0])} letras')