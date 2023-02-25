frase = str(input('Digite uma frase: '))

cont = frase.strip().lower().count('a')
pos = frase.strip().lower().find('a')+1
last = frase.strip().lower().rfind('a')+1

print(f'A letra A aparece na frase {cont} vezes, na posição {pos}. E aparece pela ultima vez na posição {last}.')