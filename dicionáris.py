jogo = {}
gols = []

jogo['Nome'] = str(input('Nome do jogador: '))
Partidas = int(input('Quantas partidas ele jogou? '))
for c in range(Partidas):
	g = (int(input(f'Quantos gols ele fez na {c+1}° partida? ')))
	gols.append(g)
	jogo['Gols'] = gols[:]
	jogo['Total'] = sum(gols)
print('==' * 30)
print(jogo)
print('==' * 30)
for k, v in jogo.items():
	print(f'{k} tem valor {v}')	
print('==' * 30)
print(f' O jogador {jogo["Nome"]} jogou {Partidas} partidas.')
for i, v in enumerate(gols):
	print(f'   -> Na {i+1} partida fez {v} gols')
print(f'Total de {jogo["Total"]} gols')
	
