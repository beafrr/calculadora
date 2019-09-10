#Complete as funcoes a seguir

def soma(a, b):
	print("A soma é igual a : ", a+b)

def subtrai(a, b):
	print("A subtração é igual a : ", a-b)

def multiplica(a, b):
	print("A multiplicação é igual a : ", a*b)

def divide(a, b):
  if(b==0):
    print("O segundo número da divisão não pode ser zero")
    b=float(input("Insira o segundo numero: "))
    print("A divisão é igual a : ", a/b)
  else:
    	print("A divisão é igual a : ", a/b)


#Programa principal

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)

