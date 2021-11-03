Exercicio favorito de Python até o momento, primeiro código que escrevi foi usando apenas o If, esse eu aprimorei com o While.

Ex 45 - Jokenpo (Curso em vídeo do Gustavo Guanabara)

import random
from random import randint
from time import sleep

opçoes = ('[0] pedra', '[1] papel', '[2] tesoura')

while True:	
	j = int(input('Escolha: [0] pedra, [1] papel, [2] tesoura '))
	if j > 2:
		print('==' * 30)
		print('Digite apenas as opções: [0] pedra, [1] papel, [2] tesoura')
		print('==' * 30)
		j = int(input('Escolha: [0] pedra, [1] papel, [2] tesoura '))	
	print('==' * 30)
	sleep(1)
	print('JO')
	sleep(1)
	print('KEN')
	sleep(1)
	print('PÔ!!!')
	print('==' * 30)
	c = random.randint(0, 2)
	print(f'Você jogou {opçoes[j]}')
	print(f'O computador jogou {opçoes[c]}')

	
	if j == c:
		print('==' * 30)
		print('Empate')
	if c == 0:
		if j == 1:
			print('==' * 30)
			print('Você venceu!!!')
		elif j == 2:
			print('==' * 30)
			print('Computador venceu!!!')
	elif c == 1:
		 if j == 0:
		 	print('==' * 30)
		 	print('Computador venceu!!!')
		 elif j == 2:
		 	print('==' * 30)
		 	print('Você venceu!!!')
	elif c == 2:
	 	if j == 0:
	 		print('==' * 30)
	 		print('Você venceu!!!')
	 	elif j == 1:
	 		print('==' * 30)
	 		print('Computador venceu!!!')
	else:
	 	 print('==' * 30)
	 	 print('Jogada invalida!')
	print('==' * 30)

	nov = str(input('Gostaria de tentar novamente? [S/N] ')).upper().strip()[0]
	print('==' * 30)
	if nov not in 'SN':
		print('Por favor responda com sim ou não ')
		print('==' * 30)
		nov = str(input('Gostaria de tentar novamente? [S/N] ')).upper().strip()[0]
		print('==' * 30) 	 
	if nov == 'N':
		break
print('Obrigada e até a proxima!')


