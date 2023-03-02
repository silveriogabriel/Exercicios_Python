'''Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
 um dos dígitos separados.'''

numero_digitado = int(input('Digite um valor: '))

unidade = numero_digitado // 1 % 10
dezena = numero_digitado // 10 % 10
centena = numero_digitado // 100 % 10
milhar = numero_digitado // 1000 % 10

print(f'Unidade : {unidade}')
print(f'Dezena : {dezena}')
print(f'Centena : {centena} ')
print(f'Milhar : {milhar}')