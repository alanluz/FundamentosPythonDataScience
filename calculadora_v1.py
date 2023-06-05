# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")


def soma(num1, num2):
	return num1+num2
def subtrai(num1, num2):
	return num1-num2
def multiplica(num1, num2):
	return num1*num2
def divide(num1, num2):
	return num1/num2
def potencia(num1, num2):
	return num1**num2
def raizQuadrada(num1):
	return num1**0.5

operacao = -1
while operacao != 0:
	print('\n------------- CALCULADORA -------------\n')
	print('OPÇÕES DISPONÍVEIS')
	print('1 - SOMAR')
	print('2 - SUBTRAIR')
	print('3 - MULTIPLICAR')
	print('4 - DIVIDIR')
	print('5 - POTENCIA')
	print('6 - RAIZ QUADRADA')
	print('0 - SAIR')
	
	
	operacao = int(input())
	if operacao == 1:
		print ('Soma escolhida')
		num1 = int(input('Digite o primeiro número: '))
		num2 = int(input('Digite o segundo número: '))
		print('A soma entre os números %r e %r é: %r' %(num1, num2, soma(num1, num2)))
	elif operacao == 2:
		print ('Subtração escolhida')
		num1 = int(input('Digite o primeiro número: '))
		num2 = int(input('Digite o segundo número: '))
		print('A subtração entre os números %r e %r é: %r' %(num1, num2, subtrai(num1, num2)))
	elif operacao == 3:
		print ('Multiplicação escolhida')
		num1 = int(input('Digite o primeiro número: '))
		num2 = int(input('Digite o segundo número: '))
		print('A multiplicação entre os números %r e %r é: %r' %(num1, num2, multiplica(num1, num2)))
	elif operacao == 4:
		print ('Divisão escolhida')
		num1 = int(input('Digite o primeiro número: '))
		num2 = int(input('Digite o segundo número: '))
		if num2 == 0:
			print('ERRO!\nO segundo número(dividendo) não pode ser zero!')
		else:
			print('A divisão entre os números %r e %r é: %r' %(num1, num2, divide(num1, num2)))
	elif operacao == 5:
		print ('Potênncia escolhida')
		num1 = int(input('Digite o primeiro número: '))
		num2 = int(input('Digite o segundo número: '))
		print('A potência de base %r e expoente %r é: %r' %(num1, num2, potencia(num1, num2)))
	elif operacao == 6:
		print ('Raiz escolhida')
		num1 = int(input('Digite o primeiro número: '))
		print('A raiz quadrada de %r é: %r' %(num1, raizQuadrada(num1)))
	elif operacao == 0:
		print ('Sair escolhida')
		print ('Até mais!')
	else:
		print('Operação não encontrada!')
		print('Por favor, digite uma operação válida')