#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “Santo”.

cidade = str(input('Digite o nome de sua cidade: ')).upper().strip().split()
print('SANTO' in cidade[0])
