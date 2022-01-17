dados = {}
lista = []
media = soma = 0
while True:
	dados['Nome'] = str(input('Nome: '))
	dados['Sexo'] = str(input('Sexo: [F/M] ')).upper().strip()[0]
	if dados["Sexo"] not in 'FM':
		print('Por favor, responda apenas F para feminino ou M para masculino')
		dados['Sexo'] = str(input('Sexo: [F/M] ')).upper().strip()[0]
	dados['Idade'] = int(input('Idade: ')) 
	soma += dados['Idade']
	lista.append(dados.copy())
	resp = str(input('Gostaria de continuar? [S/N] ')).upper().strip()[0]
	if resp not in 'SN':
		print('Por favor responda apenas com sim ou não ')
		resp = str(input('Gostaria de continuar? [S/N] ')).upper().strip()[0]
	if resp == 'N':
		break
print(f'Foram cadastradas {len(lista)} pessoas')
media = soma / len(lista)
print(f'A media de idades é igual a {media:.2f} anos')
print(f'As mulheres cadastradas foram: ',end=' ')
for i in range(0, len(lista)):
	if lista[i]['Sexo'] == 'F':
		print(f'{lista[i]["Nome"]}',end=' ')
print()
print(f'As pessoas acima da media são:',end=' ')
for i in range(0, len(lista)):
	if lista[i]['Idade'] >= media:
		print(f'{lista[i]["Nome"]}')
		print()

		
	
	