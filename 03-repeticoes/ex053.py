frase = str(input('Digite uma frase: ')).strip().lower()
frase = frase.replace(' ','')
print(f'O inverso de {frase} é {frase[::-1]}')

if frase == frase[::-1]:
    print('Sua frase é um palindromo')
else:
    print('Sua frase não é um palindromo')

