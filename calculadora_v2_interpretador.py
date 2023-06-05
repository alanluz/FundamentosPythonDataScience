def retiraEspacos(texto):
	return texto.split(" ")
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

print('\n------------- CALCULADORA -------------\n')
string = input()

lista = retiraEspacos(string)
print(lista)
num1 = float(lista[0])
operacao = lista[1]
num2 = float(lista[2])

if operacao == '+':
	print ('Soma escolhida')
	print('A soma entre os números %r e %r é: %r' %(num1, num2, soma(num1, num2)))
elif operacao == '-':
	print ('Subtração escolhida')
	print('A subtração entre os números %r e %r é: %r' %(num1, num2, subtrai(num1, num2)))
elif operacao == '*':
	print ('Multiplicação escolhida')
	print('A multiplicação entre os números %r e %r é: %r' %(num1, num2, multiplica(num1, num2)))
elif operacao == '/':
	print ('Divisão escolhida')
	if num2 == 0:
		print('ERRO!\nO segundo número(dividendo) não pode ser zero!')
	else:
		print('A divisão entre os números %r e %r é: %r' %(num1, num2, divide(num1, num2)))
elif operacao == '**' and num2 != 0.5:
	print ('Potênncia escolhida')
	print('A potência de base %r e expoente %r é: %r' %(num1, num2, potencia(num1, num2)))
elif operacao == '**' and num2 == 0.5:
	print ('Raiz quadrada escolhida')
	print('A raiz quadrada de %r é: %r' %(num1, raizQuadrada(num1)))
else:
	print('Operação não encontrada!')
	print('Por favor, digite uma operação válida')