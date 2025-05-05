import numpy as np

# Definir la matriz de transición
transition_matrix = np.array([
    [0.8, 0.15, 0.05],  # de Soleado
    [0.2, 0.7, 0.1],    # de Nublado
    [0.3, 0.4, 0.3]     # de Lluvia
])

# Estado inicial: Soleado (S)
initial_state = np.array([1, 0, 0])  # 100% Soleado

# Número de pasos (días)
steps = 2

# Realizamos la multiplicación de la matriz para 2 pasos
future_state = initial_state @ np.linalg.matrix_power(transition_matrix, steps)

# Mostrar las probabilidades de estar en cada estado después de 2 días
print(f"Probabilidades después de {steps} días: ")
print(f"Soleado: {future_state[0]:.2f}")
print(f"Nublado: {future_state[1]:.2f}")
print(f"Lluvia: {future_state[2]:.2f}")
