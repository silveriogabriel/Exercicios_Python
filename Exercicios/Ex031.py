'''Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem,cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distancia_viagem = float(input('Digite a distancia da viagem: '))
if distancia_viagem <= 200:
    print(f'Valor da viagem: {distancia_viagem*0.50}')
else:
    print(f'Valor da viagem: {distancia_viagem * 0.45}')