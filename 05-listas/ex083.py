pergunta = ''
cont = 0

pergunta = str((input('Digite uma expressão: ')))

for c in pergunta:
    if c == '(':
        cont += 1
    elif c == ')':
        cont -= 1
    if cont < 0:
        break
if cont == 0:
    print('Sua expressão está correta! ')
else:
    print('Sua expressão está errada! ')
