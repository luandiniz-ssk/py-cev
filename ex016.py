#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Exemplo: 6.127 = 6.
from math import trunc


num = float(input('Digite um valor: '))
porção_inteira = trunc(num)
print(f'A porção inteira de {num} é igual a {porção_inteira}')