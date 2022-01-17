cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
 
while True:
  n = int(input('Digite um número entre 0 e 20: '))
  if n < 0 or n > 20:
  	print('==' * 20)
  	print('Por favor, digite apenas os números que estiverem entre 0 e 20')
  	print('==' * 20)
  else:
      print('==' * 20)
      print(f'Você digitou o número {cont[n]}')
      print('==' * 20)
  nov = str(input('Você gostaria de continuar? [S/N] ')).upper().strip()[0]
  print('==' * 20)
  if nov not in 'SN':
  	print('Por favor responda apenas com sim ou não')
  	print('=='*20)
  	nov = str(input('Você gostaria de continuar? [S/N] ')).upper().strip()[0]
  	print('=='*20)
  if nov == 'N':
  	break
print('Obrigada e até a proxima!!')
