#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto: R$'))
novo_preço = preço -(preço * 5 / 100)
print(f'O produto que custava R${preço:.2f}, com 5% de desconto, passa a custar R${novo_preço:.2f}')
