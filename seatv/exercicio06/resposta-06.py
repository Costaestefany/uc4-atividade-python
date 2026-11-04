# Ler o valor da transferência bancária
valor = float(input("Digite o valor da transferência: R$ "))

# Verificar se o valor é maior que 1000
if valor > 1000:
    valor = valor + 15

# Exibir o valor total a pagar
print(f"Valor total a pagar: R$ {valor:.2f}")