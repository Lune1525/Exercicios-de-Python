import random
from time import sleep

while True:  
    j = str(input('Gostaria de jogar o dado? [S/N] ')).upper().strip()[0]
    if j == 'S':
    	print('==' * 15)
    	sleep(1)
    	c = random.randint(1, 6)
    	print(f'Você tirou o número {c}')
    	print('==' * 15)
    elif j != 'S' and j != 'N':
    	print('==' * 15)
    	print ('Digite apenas sim ou não, por favor!')
    	print('==' * 15)
    elif j == 'N':
    	break
print('==' * 15)
print('Obrigada e até a proxima!!!')
    
    

