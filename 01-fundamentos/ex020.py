import random

aluno1 = input('Qual o nome do primeiro aluno a ser sorteado? ')
aluno2 = input('Qual é o nome do segundo aluno a ser sorteado? ')
aluno3 = input('Qual é o nome do terceiro aluno a ser sorteado? ')
aluno4 = input('Qual é o nome do quarto aluno a ser sorteado? ')

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print(f'O primeiro aluno sorteado foi {lista[0]} \nSegundo aluno sorteado foi {lista[1]} \nTerceiro aluno sorteado foi {lista[2]} \nE o quarto aluno sorteado foi {lista[3]} ')

