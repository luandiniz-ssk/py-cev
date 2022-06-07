#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

quantidade_km = float(input('Digite a quantidade de quilômetros percorridos: '))
quantidade_dias = int(input('Digite por quantos dias o carro ficou alugado: '))
preço_km = quantidade_km * 0.15
preço_dias = quantidade_dias * 60
preço_total = preço_km + preço_dias
print(f'O carro foi alugado por {quantidade_dias} dias e teve uma quilometragem de {quantidade_km}KMs')
print(f'O preço toal será de R${preço_total:.2f}')
