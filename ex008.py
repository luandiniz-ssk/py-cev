#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite um valor em metros (m): '))
quilômetros = metros / 1000
hectômetros = metros / 100
decâmetros = metros / 10
decímetros = metros * 10
centímetos = metros * 100
milímetros = metros * 1000
print(f'Quilômetros: {quilômetros}')
print(f'Hectômetros: {hectômetros}')
print(f'Decâmetros: {decâmetros}')
print(f'Decímetros: {decímetros}')
print(f'Centímetros: {centímetos}')
print(f'Milímetros: {milímetros}')