#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1 = R$3.27

real = float(input('Digite quantos reais você tem: R$'))
dólar = real / 3.27
print(f'Com R${real:.2f} você poderá comprar US${dólar:.2f}')