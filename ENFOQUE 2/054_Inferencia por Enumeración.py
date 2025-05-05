# Definimos las probabilidades
P_A_Lluvia = 0.3  # Probabilidad de que llueva
P_A_No_Lluvia = 1 - P_A_Lluvia  # Probabilidad de que no llueva

P_B_Nublado_given_Lluvia = 0.8  # Probabilidad de que esté nublado dado que llueve
P_B_Nublado_given_No_Lluvia = 0.4  # Probabilidad de que esté nublado dado que no llueve

# Calculamos P(A = Lluvia, B = Nublado)
P_A_B = P_A_Lluvia * P_B_Nublado_given_Lluvia

# Calculamos P(B = Nublado) (marginalizando sobre A)
P_B = P_A_Lluvia * P_B_Nublado_given_Lluvia + P_A_No_Lluvia * P_B_Nublado_given_No_Lluvia

# Aplicamos la regla de Bayes para calcular P(A = Lluvia | B = Nublado)
P_A_given_B = P_A_B / P_B

# Mostrar el resultado
print(f"P(A = Lluvia | B = Nublado) = {P_A_given_B:.4f}")
