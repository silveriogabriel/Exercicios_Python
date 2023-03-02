'''Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

from random import choice

aluno1 = input('Digite o nome do 1 alugo: ')
aluno2 = input('Digite o nome do 2 alugo: ')
aluno3 = input('Digite o nome do 3 alugo: ')
aluno4 = input('Digite o nome do 4 alugo: ')
alunos = [aluno1,aluno2,aluno3,aluno4]
print(f'O aluno escolhido para apagar o quadro foi {choice(alunos)}')