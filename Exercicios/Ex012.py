'''Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
 com 5% de desconto.'''

valor_produto = float(input('Digite o valor do produto: '))
print(f'O valor de {valor_produto} com desconto de 5% sera de {valor_produto - (valor_produto*5/100)}')