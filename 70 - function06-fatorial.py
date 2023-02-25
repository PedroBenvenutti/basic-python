def fatorial(n, show=False):
    fat = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        fat *= c
    return fat


n1 = int(input('Digite um número: '))
print(fatorial(5, show=True))