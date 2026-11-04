# Ler a temperatura atual
temperatura = float(input("Digite a temperatura em °C: "))

# Verificar se a temperatura é maior que 35
if temperatura > 35:
    temperatura = temperatura + 5

# Exibir a temperatura final
print(f"Temperatura final: {temperatura:.1f} °C")