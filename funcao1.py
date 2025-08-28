num1= int (input('digite o primeiro numero'))
num2 =int(input ('digite o segundo numero'))
operacao= input ('digite a operacao')

def calcular (num1, num2, operacao):
    if operacao == '+':
        return num1 + num2 
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2


print(calcular(num1,num2,operacao))