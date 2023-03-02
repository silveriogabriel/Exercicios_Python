'''Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep

computador = randint(1,5)
escolha = int(input('Pensei em um numero de 1 a 5 tente adivinhar: '))
print('PENSANDO...')
sleep(1)
if computador == escolha:
    print('PARABENS ACERTOU!!')
else:
    print(f'Voce errou pensei no numero: {computador}')

