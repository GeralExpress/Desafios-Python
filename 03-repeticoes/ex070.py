
nomeproduto = pergunta = produtobarato = ''
preco = total = contador = barato = 0
texto = 'Vamos calcular as suas compras?!'

print('=' * 40)
print(f'{texto:^40}' )
print('=' * 40)

while True:
    nomeproduto = str(input('Nome do produto: '))
    preco = float(input('Qual é o preço desse produto? '))
    total += preco

    if barato == 0:
        produtobarato = nomeproduto
        barato = preco

    elif preco < barato:
        barato = preco
        produtobarato = nomeproduto

    if preco > 1000:
        contador += 1



    pergunta = str(input('Quer continuar? [s/n] ')).strip().lower()

    if pergunta == 'n':
        break

print(f'O total da compra foi R$: {total:.2f}\n'
      f'Teve {contador} produtos acima de 1000.00 reais\n'
      f'E o produto mais barato foi {produtobarato} que custa {barato:.2f}')

