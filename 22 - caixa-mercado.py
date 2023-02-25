valorun = float(input('Qual o valor do produto?: '))
condpag = int(input('Qual a condição de pagamento?: \n'
                    '1 - À vista\n'
                    '2 - Cartão\n'
                    '3 - 2x no cartão\n'
                    '4 - 3x ou mais no cartão\n'
                    'Selecione a opção desejada: '))

if condpag == 1:
    print('Selecionado pagamento à vista.')
    print(f'O valor final do produto é \033[32mR${valorun * 0.9:.2f}\033[m com desconto de 10%.')
elif condpag == 2:
    print('Selecionado pagamento em 1x no cartão.')
    print(f'O valor final do produto é de \033[32mR${valorun * 0.95:.2f}\033[m com desconto de 5%.')
elif condpag == 3:
    print('Selecionado pagamento em 2x no cartão.')
    print(f'O valor final do produto é de \033[32mR${valorun:.2f}\033[m. Parcelado em 2x de R${valorun / 2:.2f}.')
else:
    print('Selecionado a opção de parcelado.')
    parc = int(input('Parcelamos em até 6x com 20% de juros. Quantas vezes deseja parcelar?: '))
    print(f'O valor final do produto é de \033[32mR${valorun * 1.2:.2f}\033[m. Parcelado em {parc}x de R${valorun * 1.2 / parc:.2f}.')

