'''Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida 
o primeiro e o último nome separadamente.'''

nome_completo = input('Digite seu nome completo: ')
nome_split = nome_completo.split(' ')
print(F'O primeiro nome foi {nome_split[0]} e o segundo {nome_split[-1]}')