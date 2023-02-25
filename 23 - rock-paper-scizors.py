import random

print('\033[4;31m===JOKENPÔ===\033[m')

opcao = str(input('PEDRA? PAPEL? TESOURA? '))

lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = random.choice(lista)

if opcao.format().strip().upper() == 'PEDRA' and pc == 'TESOURA':
    print(f'Você selecionou PEDRA. O computador selecionou {pc}.\nVOCÊ GANHOU!!!')
elif opcao.format().strip().upper() == 'TESOURA' and pc == 'PAPEL':
    print(f'Você selecionou TESOURA. O computador selecionou {pc}.\nVOCÊ GANHOU!!!')
elif opcao.format().strip().upper() == 'PAPEL' and pc == 'PEDRA':
    print(f'Você selecionou PAPEL. O computador selecionou {pc}.\nVOCÊ GANHOU!!!')
elif opcao.format().strip().upper() == pc:
    print(f'Você selecionou {opcao.format().strip().upper()} e o Computador selecionou {pc}.\nEMPATE!')
else:
    print(f'Você selecionou {opcao.format().strip().upper()} e o Computador selecionou {pc}.\nVOCÊ PERDEU')






