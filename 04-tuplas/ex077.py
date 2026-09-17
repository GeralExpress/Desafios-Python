palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro', 'lorena')

for c in range(0, len(palavras)):
    nome = palavras[c].upper()
    print()
    print(f' Na palavra {nome} temos as vogais:', end ='' )
    for letra in nome:
        if letra in 'AEIOU':
            print(f'\033[1;31m{letra}\033[m', end=' ')
