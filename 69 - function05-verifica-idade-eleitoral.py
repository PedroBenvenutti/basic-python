def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 18:
        return f'Com {idade} você tem: VOTO NEGADO!'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} você tem: VOTO OBRIGATÓRIO!'
    elif idade >= 65:
        return f'Com {idade} você tem: VOTO OPCIONAL!'

nasc = int(input('Qual seu ano de nascimento? '))
print(voto(nasc))
