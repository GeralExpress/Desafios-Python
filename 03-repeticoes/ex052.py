
n = int(input('Escolha um número! '))

d = 0
print('Os números em vermelhos são os números diviseis:')

for c in range(1, n + 1):
    if n % c == 0:
        d += 1
        print(f'\033[31m{c}\033[m', end = ' ')
    else:
        print(c, end = ' ')
print()
if d == 2:
    print('Seu número é primo!')
else:
    print('Seu número não é primo!')
