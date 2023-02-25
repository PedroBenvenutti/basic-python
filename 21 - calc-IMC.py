altura = float(input('Insira sua altura: '))
peso = float(input('Insira seu peso: '))


imc = peso / altura ** 2

print(f'O seu IMC é de {imc:.2f}')
if imc <= 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc <=25:
    print('Peso Ideal.')
elif imc > 25 and imc <= 30:
    print('Sobrepeso.')
elif 30 < imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida')

print('---------------')
print('Abaixo de 18.5 = Abaixo do peso.')
print('Entre 18.5 e 25: Peso Ideal.')
print('Entre 25 e 30: Sobrepeso.')
print('Entre 30 e 40: Obesidade.')
print('Acima de 40: Obesidade móbida.')
print('---------------')