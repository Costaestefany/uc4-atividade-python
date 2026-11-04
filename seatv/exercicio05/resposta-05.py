# Ler a quantidade atualizada em estoque
quantidade = float(input("Digite a quantidade em estoque: "))

# Verificar se a quantidade é menor que 20
if quantidade <= 20:
    quantidade = quantidade + 50

# Exibir a quantidade atualizada
print(f"Quantidade atualizada no estoque: {quantidade}")