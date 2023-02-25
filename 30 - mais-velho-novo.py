idademedia = 0
somaidade = 0
menores = 0
homem = 0
velho = 0
nomevelho = 0
for c in range(1, 5):
    print(f'-----{c}ª pessoa.-----')
    nome = str(input('Insira o nome: '))
    idade = float(input('Insira a idade: '))
    sexo = int(input('Insira o sexo: \n1 - Masculino\n2 - Feminino\nOpção: '))
    somaidade += idade
    if c == 1 and sexo == 1:
        velho = idade
        nomevelho = nome
    else:
        if velho < idade:
            velho = idade
            nomevelho = nome
    if sexo == 2 and idade <= 20:
        menores += 1
idademedia = somaidade / 4
print(f'O homem mais velho é {nomevelho} com {velho} anos.')
print(f'A idade média do grupo é de {idademedia} anos.')
print(f'O número de mulheres menores que 20 anos é de {menores} mulheres.')

