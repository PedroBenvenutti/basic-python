def notas(*num, sit=False):
    """
    Função para analisar notas e situações de varios alunos.
    :param num: uma ou mais notas
    :param sit: parametro opcional indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = {'Quantidade de notas':len(num), 'Maior Nota':max(num), 'Menor Nota':min(num), 'Média': sum(num)/len(num)}
    if sit == True:
        if dados['Média'] >= 7:
            dados['Situação']='BOA'
        elif 6 <= dados['Média'] < 7:
            dados['Situação']='Razoável'
        else:
            dados['Situação']='RUIM'
    return dados


#Programa Principal
resp = notas(5.5, 9, 6, 7, 8, 5, 10, 8, sit=True)
print(resp)
help(notas)
