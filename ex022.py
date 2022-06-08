#Crie um programa que leia o nome completo de uma pessoa e mostre;
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras tem ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
nome_maiúsculo = nome.upper()
nome_minúsculo = nome.lower()
nome_separado = nome.split()
nome_junto = ''.join(nome_separado)
primeiro_nome = nome_separado[0]
print('Analisando seu nome...')
print(f'Apenas maiúsculas: {nome_maiúsculo}')
print(f'Apenas minúsculas: {nome_minúsculo}')
print(f'Seu nome tem {len(nome_junto)} letras')
print(f'O seu primeiro nome é {primeiro_nome}')
