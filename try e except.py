def leiaint(msg):
	while True:
		try:
			n = int(input(msg))
		except (ValueError, TypeError):
			print('\033[31mErro! Digite um valor inteiro valido.\033[m')
			continue
		else:
			return n
			
def leiafloat(msg):
			while True:
				try:
					nf = float(input(msg))
				except(ValueError, TypeError):
					print('\033[31mErro! Digite um valor inteiro valido.\033[m')
					continue
				else:
					return nf
			
		
num = leiaint('Digite um número inteiro: ')
numf = leiafloat('Digite um número real: ')
print(f'Valor digitado foi {num}')
print(f'Valor digitado foi {numf}')