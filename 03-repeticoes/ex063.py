print('Sequencia Fibonacci')
print('<>'* 20)

quantos = int(input('Quantos termos deseja mostrar: '))
cont = 0
a = 0
b = 1

while cont < quantos:
    print(a, end='')
    cont += 1
    print(' => ' if cont < quantos else '', end='')
    c = a + b
    a = b
    b = c

