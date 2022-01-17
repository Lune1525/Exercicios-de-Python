import random 
from random import randint
n = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f'Foram sorteados os números {n}\nDesses valores o menor é o {min(n)} e maior é o {max(n)}')