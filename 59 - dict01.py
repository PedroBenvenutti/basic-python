escola = {}

escola['nome'] = str(input('Aluno: '))
escola['media'] = float(input('Média: '))
if escola['media'] >= 7:
    escola['situação'] = 'Aprovado'
else:
    escola['situação'] = 'Reprovado'
print(f'O aluno {escola["nome"]} teve a média de {escola["media"]}.')
print(f'Aluno {escola["situação"]}')