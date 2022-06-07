#Escreva um programa que converta uma temperatura digitada em °C e transforme-a em °F.

graus_celsius = float(input('Digite a temperatura em °C: '))
graus_fahrenheit = (graus_celsius * 9 / 5) + 32
print(f'Com {graus_celsius}°C, a temperatura em graus fahrenheits é de {graus_fahrenheit:.2f}°F')
