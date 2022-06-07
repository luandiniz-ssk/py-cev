#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('Digite seu salário: R$'))
novo_salário = salário + (salário * 15 / 100)
print(f'O seu salário era R${salário:.2f}, e com um aumento de 15%, passa a ser de R${novo_salário:.2f}')
