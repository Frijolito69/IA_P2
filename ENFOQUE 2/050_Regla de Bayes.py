# Datos de probabilidad
P_A = 0.01    # Probabilidad a priori de tener la enfermedad
P_B_given_A = 0.9  # Probabilidad de que el test sea positivo dado que tienes la enfermedad
P_B = 0.1     # Probabilidad total de que el test sea positivo

# Aplicamos la Regla de Bayes para calcular la probabilidad posterior
P_A_given_B = (P_B_given_A * P_A) / P_B

# Mostrar el resultado
print(f"La probabilidad de tener la enfermedad dado que el test es positivo: {P_A_given_B:.2f}")
