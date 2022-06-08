#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice

primeiro_aluno = str(input('Digite o nome do primeiro aluno: '))
segundo_aluno = str(input('Digite o nome do segundo aluno: '))
terceiro_aluno = str(input('Digite o nome do terceiro aluno: '))
quarto_aluno = str(input('Digite o nome do quarto aluno: '))
alunos = (primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno)
escolhido = choice(alunos)
print(f'O aluno escolhido foi {escolhido}')
