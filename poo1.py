class cat:
	def __init__(self, name):
		self.name = name
		print(f'{self.name} its a nice name!')
		
	def weight_cat(self, weight):
		self.weight = weight
		if (self.weight > 5):
			print('warning! your cat its overweight!')
		elif (self.weight > 3.0 and self.weight < 5):
			print('Everything fine')
		else:
			print('warning! your cat its underweight!')
			
    def _diet_cat(self):
	 	self.msg = 'The feed its fine!'
	 	if (self.weight > 5.0):
	 		self.msg = 'Give him more feed'
	 	if (self.weight < 3.5):
	 		self.msg = 'Give him less feed'
	 	return self.msg
	 	
    def info_cat(self):
	 	print(f'The {self.name} its {self.weight} KG')
	 	print(self._diet_cat())
	 	
		
		
cat_name = input('Whats the cats name? ')
g1 = cat(cat_name)
weight = float(input(f'Whats the weight of {cat_name} [KG] '))
g1.weight_cat(weight)
g1.info_cat()