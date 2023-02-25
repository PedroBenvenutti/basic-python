pessoas = {'nome':'Gustavo', 'Sexo': 'M', 'idade': 22}
pessoas['Peso'] = 98 #adiciona elemento
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k) #printa todas as chaves do dicionario

for k, v in pessoas.items():
    print(f'{k} = {v}') #printa chaves e valores

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla:'))
    brasil.append(estado.copy()) #tem que ser usado o metodo copy, o [:] não funciona com dict
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')