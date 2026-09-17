lista = []
valor = comp = 0

for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    for n, i in enumerate(lista):
        if valor < i:
            lista.insert(n, valor)
            print(f'Adicionado na posição {n} da lista...')
            break
    else:
        if valor > lista[-1]:
            lista.append(valor)
            print(f'Adicionado ao final da lista...')

print(lista)

# 10 5 3 4
