lista = []
num = cont  = 0
pergunta = ''

while True:
    num = int(input('Digite um número: '))
    cont += 1
    if cont == 1:
        lista.append(num)
    else:
        for i, v in enumerate (lista):
            if num > v:
                lista.insert(i, num)
                break
        else:
            lista.append(num)

    pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if pergunta == 'N':
        break
print('*' * 40)
print(f'Números que foram digitados: {cont} números!' )
print(f'A lista em ordem decrescente é: {lista}' )
if 5 in lista:
    print('O Número 5 faz parte da lista!')
else:
    print('O Número 5 não faz parte da lista!')
#10 1 3 600 5

#Estou tentando colocar em ordem decrescente sem usar comando proprio para isso.
