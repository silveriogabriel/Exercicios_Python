'''Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

valor_inteiro = int(input('Digite um valor inteiro: '))

if valor_inteiro//2 == 0:
    print('Par')
else:
    print('Impar')