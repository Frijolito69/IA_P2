import numpy as np

# Matrices de transición, emisión y probabilidades iniciales
P = np.array([[0.7, 0.3],  # Matriz de transición
              [0.4, 0.6]])

E = np.array([[0.9, 0.1],  # Matriz de emisión
              [0.2, 0.8]])

pi = np.array([0.5, 0.5])  # Probabilidades iniciales

# Observaciones (0: O1, 1: O2)
observaciones = [0, 1, 0, 1, 0]

# Número de estados y observaciones
N = len(pi)
T = len(observaciones)

# Fase hacia adelante
alpha = np.zeros((T, N))
for i in range(N):
    alpha[0, i] = pi[i] * E[i, observaciones[0]]

for t in range(1, T):
    for i in range(N):
        alpha[t, i] = np.sum(alpha[t-1] * P[:, i]) * E[i, observaciones[t]]

# Fase hacia atrás
beta = np.zeros((T, N))
beta[T-1] = np.ones(N)

for t in range(T-2, -1, -1):
    for i in range(N):
        beta[t, i] = np.sum(P[i, :] * E[:, observaciones[t+1]] * beta[t+1])

# Cálculo del suavizado
gamma = np.zeros((T, N))
for t in range(T):
    for i in range(N):
        gamma[t, i] = alpha[t, i] * beta[t, i]
    gamma[t] /= np.sum(gamma[t])

# Mostrar los resultados
print("Probabilidades suavizadas de los estados:")
for t in range(T):
    print(f"Tiempo {t}: Estado A: {gamma[t, 0]:.4f}, Estado B: {gamma[t, 1]:.4f}")
