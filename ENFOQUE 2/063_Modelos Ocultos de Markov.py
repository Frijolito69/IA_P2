import numpy as np

# Definición de matrices y probabilidades iniciales
A = np.array([[0.7, 0.3],  # Matriz de transición
              [0.4, 0.6]])

B = np.array([[0.9, 0.1],  # Matriz de emisión
              [0.2, 0.8]])

pi = np.array([0.5, 0.5])  # Probabilidades iniciales

# Secuencia de observaciones (0: O1, 1: O2)
observaciones = [0, 1, 0]  # O1, O2, O1

# Número de estados y observaciones
N = len(pi)
T = len(observaciones)

# Fase hacia adelante (Forward)
alpha = np.zeros((T, N))

# Inicialización
for i in range(N):
    alpha[0, i] = pi[i] * B[i, observaciones[0]]

# Cálculo hacia adelante
for t in range(1, T):
    for i in range(N):
        alpha[t, i] = np.sum(alpha[t-1] * A[:, i]) * B[i, observaciones[t]]

# Cálculo de la probabilidad de la secuencia observada
probabilidad = np.sum(alpha[T-1, :])

print(f"Probabilidad de la secuencia observada: {probabilidad:.4f}")
