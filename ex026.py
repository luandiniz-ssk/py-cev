#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra “A”
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip().upper()
quantidade = frase.count('A')
primeira_vez = frase.find('A')
última_vez = frase.rfind('A')
print(f'Aparecem {quantidade} letras "A" na frase')
print(f'Aparece pela primeira vez na {primeira_vez + 1}° posição')
print(f'Aparece pela última vez na {última_vez + 1}° posição')
