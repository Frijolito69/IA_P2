# Datos de probabilidad
P_A = 0.3  # Probabilidad de lluvia
P_B_given_A = 0.6  # Probabilidad de aparcar dado que llueve
P_C_given_A_B = 0.2  # Probabilidad de accidente dado lluvia y aparcar

# Aplicamos la regla de la cadena para calcular la probabilidad conjunta
P_ABC = P_A * P_B_given_A * P_C_given_A_B

# Mostrar el resultado
print(f"La probabilidad conjunta de lluvia, aparcar y accidente es: {P_ABC:.4f}")
