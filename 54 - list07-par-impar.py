par = []
impar = []
database = [impar, par]

for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor:'))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

par.sort()
impar.sort()
print(database)

