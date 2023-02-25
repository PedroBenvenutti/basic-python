import math
adj = float(input('Insira o valor do cateto adjacente: '))
op = float(input('Insira o valor do cateto oposto: '))
hip = math.hypot(adj, op)

print(hip)
