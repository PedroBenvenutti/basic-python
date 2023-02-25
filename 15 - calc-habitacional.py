print('\033[4;31mCALCULADORA HABITACIONAL\033[m\n')

valorcasa = float(input('Informe o valor total do imóvel: '))
salario = float(input('Informe seu salário bruto: '))
parcelas = int(input('Informe em quantos anos você quer financiar o imóvel: '))
prestacaom = valorcasa / (parcelas * 12)

if prestacaom > salario * 0.30:
    print(f'Não foi possível fazer o empréstimo. O valor da parcela de \033[31mR${prestacaom:.2f}\033[m excede os \033[31m30%\033[m limite do seu salário. É necessário aumentar o número de parcelas.')

else:
    print(f'O valor da parcela ficará em \033[33mR${prestacaom:.2f}\033[m. Podemos prosseguir?')

