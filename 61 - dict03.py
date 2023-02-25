from datetime import date
hoje = date.today()
dados = {}
dados['nome'] = str(input('Qual seu nome?: '))
dados['nasc'] = int(input('Qual o ano de nascimento?: '))
dados['idade'] = (hoje.year - dados['nasc'])
dados['carteira'] = int(input('Informe o Nº da carteira de trablho [digite 0 se não possuir]: '))
if dados['carteira'] != 0:
    dados['contratacao'] = int(input('Informe o ano de contratação: '))
    dados['salario'] = float(input('Informe o salário: '))
    dados['aposenta'] = (dados['contratacao'] - dados['nasc']) + 35

for k, v in dados.items():
    print(f'O {k} é {v}')
