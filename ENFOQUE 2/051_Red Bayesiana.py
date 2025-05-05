# Probabilidades
P_A = 0.3  # Probabilidad de lluvia
P_B_given_A = 0.2  # Probabilidad de aparcar dado que llueve
P_C_given_A_T = 0.7  # Probabilidad de accidente dado lluvia y tráfico

# Calcular la probabilidad de accidente dado lluvia y tráfico
P_C = P_C_given_A_T * P_A

# Mostrar el resultado
print(f"La probabilidad de accidente dado que llueve y hay tráfico es: {P_C:.2f}")
