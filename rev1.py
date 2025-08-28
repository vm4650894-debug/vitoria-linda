idade = int(input("Digite sua idade: "))


estudante = input("É estudante? (s/n): ").lower()

if idade <= 12:
    preco = 8.00
elif estudante == 's':
    preco = 12.00
elif idade >= 65:
    preco = 10.00
else:
    preco = 20.00

print(f"Preço do ingresso: R$ {preco:.2f}")