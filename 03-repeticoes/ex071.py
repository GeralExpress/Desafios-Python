from time import sleep

valorsacado = total = total50 = total20 = total10 = total1 = 0

print('Caixa do cazaquistao!')
print('-'*40)


while True:
    valorsacado = int(input('Qual valor você deseja sacar? [somente valores inteiros!] R$: '))
    total = valorsacado
    
    total50 = valorsacado // 50
    multi = valorsacado - (total50 * 50)
    valorsacado = multi


    total20 = valorsacado // 20
    multi = valorsacado - (total20 * 20)
    valorsacado = multi

    total10 = valorsacado // 10
    multi = valorsacado - (total10 * 10)
    valorsacado = multi

    total1 = valorsacado // 1

    break

print(f'Retirando {total50} cedulas de 50 reais...')
sleep(1)
print(f'Retirando {total20} cedulas de 20 reais...')
sleep(1)
print(f'Retirando {total10} cedulas de 10 reais...')
sleep(1)
print(f'Retirando {total1} cedulas de 1 real...')
sleep(1)

print(f'Total de {total} em cedulas...Volte Sempre!.')