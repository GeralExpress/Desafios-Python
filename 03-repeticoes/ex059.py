val = 0

soma = 0
mult = 0
maior = 0

num1 = int(input('Escolha um número: '))
num2 = int(input('Escolha outro número: '))


while val != 5:
    escolha = int(input(
          '[1] SOMAR\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR NÚMERO\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] TERMINAR PROGRAMA\n'
        'Digite a sua escolha!: '))
    if escolha == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} mais {num2} é {soma}')
    elif escolha == 2:
        mult = num1 * num2
        print(f'A multiplicação de {num1} vezes {num2} é {mult}')
    elif escolha == 3:
        if num1 > maior and num1 > num2:
            maior = num1
            print(f'O maior número entre {num1} e {num2} é {maior}')
        else:
            maior = num2
            print(f'O maior número entre {num1} e {num2} é {maior}')
    elif escolha == 4:
        maior = 0
        num1 = int(input('Digite novamente o primeiro valor: '))
        num2 = int(input('Digite novamente o segundo valor: '))
    elif escolha == 5:
        val = 5
    else:
        print('\033[1;31mOpção invalída! Tente novamente\033[m')
    print('='*40)
print('Você encerrou o programa! :(')