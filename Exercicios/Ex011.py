'''Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
 calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta 
 pinta uma área de 2 metros quadrados.'''

largura = float(input('Digite a largura da parede'))
altura = float(input(f'Digite a altura da parede: '))
area = altura * largura
print(f'Para pintar toda area de {area} Sera nescessario {(area/2)} L de tinta')