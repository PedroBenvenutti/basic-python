largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura * altura
tinta = area / 2

print(f'\033[40mA área da parede é de {area} metros quadrados\033[m')
print(f'\033[40mSerá necessário {tinta} litros de tinta para pintar a parede.\033[m')