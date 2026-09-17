a = int(input('Digite o primeiro valor do triângulo: '))
b = int(input('Digite o segundo valor do triângulo: '))
c = int(input('Digite o terceiro valor do triângulo: '))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print('Eles pode formar um triângulo! EQUILATERO')
    elif a == b or b == c or c == a:
        print('Eles pode formar um triângulo! ISÓSCELES')
    elif a != b and b != c and  a != c:
        print('Eles pode formar um triângulo! ESCALENO')
else:
    print('Eles não podem formar um triângulo! ')
