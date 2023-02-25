print('-' * 20)
print('\033[4;35mCADASTRO DE CLIENTE\033[m')
print('-' * 20)
continuar = ''
conth = contm = conti = 0

while True:
    idade = int(input('Informe a idade: '))
    while (idade < 0) or (idade > 120):
        idade = int(input('Informe a idade de no máximo 120 anos: '))
    sexo = str(input('Informe o sexo: [M] [F]')).upper().strip()
    while (sexo != 'M') and (sexo != 'F'):
        sexo = str(input('Informe o sexo: \033[1;31mApenas [M] [F]\033[m')).upper().strip()
    continuar = str(input('Deseja cadastrar mais pessoas?: [S] [N]')).upper().strip()
    while continuar not in 'SN': #melhor opção para verificar
        continuar = str(input('Deseja cadastrar mais pessoas?: [S] [N]')).upper().strip()
    if idade >= 18:
        conti += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm += 1
    if continuar == 'N':
        break
print(f'A quantidade de pessoas maiores de 18 anos é de {conti}.')
print(f'A quantidade de homens cadastrados é de {conth}.')
print(f'A quantidade de mulheres menores de 20 anos é de {contm}')

