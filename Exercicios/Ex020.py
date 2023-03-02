'''Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de
 trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle


aluno1 = input('Digite o nome do 1 alugo: ')
aluno2 = input('Digite o nome do 2 alugo: ')
aluno3 = input('Digite o nome do 3 alugo: ')
aluno4 = input('Digite o nome do 4 alugo: ')
alunos = [aluno1,aluno2,aluno3,aluno4]
shuffle(alunos)
print(f'A ordem para apagar o quadro sera : {alunos}')