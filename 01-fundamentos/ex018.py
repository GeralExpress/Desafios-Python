from math import sin, cos, tan, radians

angulo = float(input('Digite um angulo: '))

radians = radians(angulo)
cosseno = cos(radians)
tangente = tan(radians)
seno = sin(radians)

print(f'O ângulo de {angulo} tem o SENO de {seno:.2f} \nO ângulo de {angulo} tem o COSSENO de {cosseno:.2f} \n O ângulo de {angulo} tem a TANGENTE de {tangente:.2f} ')