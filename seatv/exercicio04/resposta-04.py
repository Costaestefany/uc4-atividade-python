# Ler a pontuação atual
pontuacao = float(input("Digite a sua pontuação: "))

# Verificar se a pontuação é maior a 500
if pontuacao >= 500:
    pontuacao = pontuacao + 100

# Exibir a pontuação final
print(f"Pontuação final: {pontuacao:.1f}")