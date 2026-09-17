lista = []
pares = []
impares = []

pergunta = ''


while True:
    lista.append(int(input('Digite um valor: ')))
    pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if pergunta == 'N':
        break

for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'Os números da sua lista são: {lista}')
print(f'Os números pares da lista foram: {pares}')
print(f'Os números impares da lista foram: {impares}')
