#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip().split()
primeiro_nome = nome[0]
último_nome = nome[-1]
print(f'Primeiro nome: {primeiro_nome}')
print(f'Último nome: {último_nome}')
