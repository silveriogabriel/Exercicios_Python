'''Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade_carro = float(input('Digite a velocidade do carro: '))
if velocidade_carro > 80:
    print(f'Voce foi multado em {(velocidade_carro - 80) * 7:.2f}R$ Por ultrapaçar 80Km/h')
else:
    print('Tenha uma boa viajem!!')