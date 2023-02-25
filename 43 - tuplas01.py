tupla = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')


while True:
    n = int(input('Digite um número entre 0 e 20:'))
    if 0 <= n <= 20:
        break
print(f'Você digitou o número {tupla[n]}.')


