lanche = 'Hamburguer' , 'Suco', 'Pizza', 'Pudim'
print(sorted(lanche)) #função que ordena alfabéticamente

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')

for comida in lanche:
    print(f'Eu vou comer {comida}.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#______________________

a = 2, 5, 4
b = 5, 8, 1, 2
c = a + b #concactena a e b
print(c.count(5))
print(c.index(8))