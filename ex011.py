#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input('Digite a altura da parede (m): '))
largura = float(input('Digite a largura da parede (m): '))
área = altura * largura
tinta = área / 2
print(f'Com uma parede de {altura:.2f}x{largura:.2f}, sua área é {área:.2f}m², e será necessário {tinta:.2f}L para pintá-la')