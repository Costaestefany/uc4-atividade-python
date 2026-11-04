# Ler o valor total da compra
valor = float(input("Digite o valor da compra: R$ "))

# Verificar se o valor é maior que 200
if valor > 200:
    valor = valor - 30

# Exibir o valor final a pagar
print(f"Valor a pagar: R$ {valor:.2f}")