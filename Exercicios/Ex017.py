'''Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto 
adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''


from math import hypot

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjecente = float(input('Digite o cateto Adjecente: '))

print(f'O valor da hipotenuza resulta em: {hypot(cateto_oposto,cateto_adjecente)}')