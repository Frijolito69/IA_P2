import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
A = 1  # Matriz de transición de estado
H = 1  # Matriz de observación
Q = 0.1  # Varianza del ruido del proceso
R = 1  # Varianza del ruido de observación
x_true = 2  # Valor real del estado (esto es lo que queremos estimar)

# Número de pasos de tiempo
n = 50

# Generar el proceso y las observaciones ruidosas
np.random.seed(0)
x_real = np.zeros(n)
z = np.zeros(n)
x_real[0] = x_true
z[0] = H * x_real[0] + np.random.normal(0, R)

for t in range(1, n):
    x_real[t] = A * x_real[t-1] + np.random.normal(0, Q)
    z[t] = H * x_real[t] + np.random.normal(0, R)

# Inicialización del filtro de Kalman
x_est = np.zeros(n)  # Estimación del estado
P = np.zeros(n)  # Error de estimación
x_est[0] = 0  # Estimación inicial
P[0] = 1  # Error de estimación inicial

# Aplicar el filtro de Kalman
for t in range(1, n):
    # Predicción
    x_pred = A * x_est[t-1]
    P_pred = A * P[t-1] * A + Q
    
    # Corrección
    K = P_pred * H / (H * P_pred * H + R)
    x_est[t] = x_pred + K * (z[t] - H * x_pred)
    P[t] = (1 - K * H) * P_pred

# Graficar los resultados
plt.plot(x_real, label="Estado Real")
plt.plot(x_est, label="Estimación del Filtro de Kalman", linestyle='--')
plt.plot(z, label="Observaciones", linestyle=':')
plt.legend()
plt.xlabel("Tiempo")
plt.ylabel("Valor del Estado")
plt.title("Filtro de Kalman: Estimación y Observación")
plt.show()
