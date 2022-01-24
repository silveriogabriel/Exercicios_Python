'''Faça um programa que leia algo pelo teclado mostre seu tipo primitivo e todas as informacoes sobre ele'''

leitura = input('Digite algo pelo teclado: ')
print(f'O tipo primitivo é {type(leitura)}')
print(f'O valor composto por numeros? {leitura.isnumeric()}')
print(f'O valor é composto por numeros e letras? {leitura.isalnum()}')
print(f'O valor é composto apenas por espacos ? {leitura.isspace()}')
print(f'O valor é composto apenas por letras? {leitura.isalpha()}')
print(f'O composto é um numero decimal? {leitura.isdecimal()}')