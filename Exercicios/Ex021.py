'''Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome_completo = input('Digite seu nome completo: ')

print(f'Em maiusculas: {nome_completo.upper}')
print(f'Em minusculas: {nome_completo.lower}')
print(f'Numero de letras: {len(nome_completo)}')
primeiro_nome = nome_completo.split(' ')
print(f'Primeiro nome tem: {len(primeiro_nome[0])}')