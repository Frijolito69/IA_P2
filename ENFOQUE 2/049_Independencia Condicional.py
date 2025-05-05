# Probabilidades iniciales
P_A = 0.7  # Probabilidad de lluvia
P_B = 0.5  # Probabilidad de llevar paraguas
P_C = 0.8  # Probabilidad de conocer el pronóstico

# Dado el pronóstico, la probabilidad de lluvia y llevar paraguas son independientes
P_A_dado_C = P_A  # Probabilidad de lluvia, dado que conocemos el pronóstico
P_B_dado_C = P_B  # Probabilidad de paraguas, dado que conocemos el pronóstico

# Resultados
print(f"Probabilidad de lluvia dado el pronóstico: {P_A_dado_C:.2f}")
print(f"Probabilidad de paraguas dado el pronóstico: {P_B_dado_C:.2f}")
