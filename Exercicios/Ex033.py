'''Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = float(input('Digite um primeiro valor: '))
n2 = float(input('Digite um segundo valor: '))
n3 = float(input('Digite um terceiro valor: '))
maior = n1
if maior < n2 :
    maior = n2
if maior < n3:
    maior = n3
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n2


print(f'Maior valor é {maior} Menor é : {menor} !')