'''Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
cosseno e tangente desse ângulo.'''

from math import sin,cos,tan

valor = float(input('Digite um ângulo para ver seus valores: '))

print(f'O valor do seno é {sin(valor)}')
print(f'Sua tangente é {tan(valor)}')
print(f'Seu cosseno é {cos(valor)}')
