'''Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''

nome_cidade = input('Digite o nome da sua cidade: ').strip()

print(nome_cidade[:5].upper() == 'SANTO')