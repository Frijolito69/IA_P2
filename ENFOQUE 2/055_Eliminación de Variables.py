# Definimos las probabilidades
P_A_Lluvia = 0.3  # Probabilidad de que llueva
P_A_No_Lluvia = 1 - P_A_Lluvia  # Probabilidad de que no llueva

P_B_given_A = 0.8  # Probabilidad de que esté nublado dado que llueve
P_B_given_No_Lluvia = 0.4  # Probabilidad de que esté nublado dado que no llueve

P_C_given_A = 0.7  # Probabilidad de que haga frío dado que llueve
P_C_given_No_Lluvia = 0.2  # Probabilidad de que haga frío dado que no llueve

P_C_given_B = 0.5  # Probabilidad de que haga frío dado que está nublado

# Paso 1: Eliminamos la variable C sumando sobre todas sus posibles instancias
P_A_B = P_A_Lluvia * P_B_given_A * P_C_given_A + P_A_No_Lluvia * P_B_given_No_Lluvia * P_C_given_No_Lluvia

# Paso 2: Calculamos P(B), la probabilidad marginal de B
P_B = P_A_Lluvia * P_B_given_A * P_C_given_A + P_A_No_Lluvia * P_B_given_No_Lluvia * P_C_given_No_Lluvia

# Paso 3: Aplicamos la regla de Bayes para calcular P(A | B)
P_A_given_B = P_A_B / P_B

# Mostrar el resultado
print(f"P(A = Lluvia | B = Nublado) = {P_A_given_B:.4f}")
