# Ler o salário do funcionário
salario = float(input("Digite o salário: R$ "))

# Verificar se o salário é menor que 1500
if salario < 1500:
    salario = salario + 200

# Exibir o salário final
print(f"Salário final: R$ {salario:.2f}")