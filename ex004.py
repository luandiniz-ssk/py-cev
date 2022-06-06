#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

qualquer_coisa = input('Digite alguma coisa: ')
print(f'Tipo primitivo: {type(qualquer_coisa)}')
print(f'Apenas letras: {qualquer_coisa.isalpha()}')
print(f'Apenas números: {qualquer_coisa.isnumeric()}')
print(f'Alfanumérico: {qualquer_coisa.isalnum()}')
print(f'Decimal: {qualquer_coisa.isdecimal()}')
print(f'Apenas maisculas: {qualquer_coisa.isupper()}')
print(f'Apenas miunsculas: {qualquer_coisa.islower()}')
print(f'Apenas espaços: {qualquer_coisa.isspace()}')
print(f'Está capitalizado: {qualquer_coisa.istitle()}')
