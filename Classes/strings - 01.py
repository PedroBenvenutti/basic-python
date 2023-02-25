frase = '   Curso em Vídeo Python   '
#strip tira os espaços antes e depois e troca Python por Java
print(frase.strip().replace('Python', 'Java'))
print(frase.count('o'))
print('Curso' in frase)

#transforma em lower e busca vídeo
print(frase.lower().find('vídeo'))

#coloca a frase dentro da variavel dividido e splita ela em lista
dividido = frase.split()
print(dividido)
