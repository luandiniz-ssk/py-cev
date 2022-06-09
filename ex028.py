#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)

print('Sou seu computador e pensei em um valor entre 0 e 5...Consegue adivinhar?')
sleep(2.8)

jogador = int(input('Seu palpite: '))
if jogador == computador:
    print(f'Acertou! O número que pensei era o {computador}')
else:
    print(f'Errou! O número que eu pensei era o {computador}')
