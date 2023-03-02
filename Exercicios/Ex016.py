'''Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado 
e mostre na tela a sua porção Inteira.'''

from math import trunc

numero_real = float(input('Digite um valor real: '))
print(f'A porção inteira do valor {numero_real} resulta em {trunc(numero_real)}')