#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

primeiro_aluno = str(input('Digite o nome do primeiro aluno: '))
segundo_aluno = str(input('Digite o nome do segundo aluno: '))
terceiro_aluno = str(input('Digite o nome do terceiro aluno: '))
quarto_aluno = str(input('Digite o nome do quarto aluno: '))
alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
shuffle(alunos)
print(f'A ordem de apresentação foi: {alunos}')
