'''Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
 e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
  por dia e R$0,15 por Km rodado'''

kilometros_percorridos = float(input('Digite a quantidade de KM: '))
dias_aluguel = float(input('Digite a quantidade de dias alugados: '))

print(f'''Voce rodou {kilometros_percorridos}KM e passou {dias_aluguel} com o veiculo,
O valor a pagar é de {(kilometros_percorridos * 0.15)+(dias_aluguel * 60)}R$''')