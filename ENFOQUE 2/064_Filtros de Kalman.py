import numpy as np

# Parámetros del modelo
F = np.array([[1, 1],  # Matriz de transición de estado (predice la posición y velocidad)
              [0, 1]]) 

H = np.array([[1, 0]])  # Matriz de observación (solo observamos la posición)

Q = np.array([[1, 0],   # Covarianza del ruido del proceso (supuesto ruido pequeño)
              [0, 1]])

R = np.array([[10]])  # Covarianza del ruido de medición (sensor ruidoso)

P = np.array([[1, 0],  # Matriz de covarianza inicial (suposición sobre la incertidumbre inicial)
              [0, 1]])

x = np.array([[0],  # Estimación inicial del estado (posición, velocidad)
              [1]])

# Simulación de un conjunto de observaciones (posiciones medidas por un sensor)
z = [5, 6, 7, 8, 9]  # Mediciones de la posición a lo largo del tiempo

# Filtro de Kalman
for k in range(len(z)):
    # Predicción
    x_pred = np.dot(F, x)  # Predicción del estado
    P_pred = np.dot(np.dot(F, P), F.T) + Q  # Predicción de la covarianza

    # Actualización (si se recibe una nueva observación)
    y = z[k] - np.dot(H, x_pred)  # Innovación (diferencia entre la medición y la predicción)
    S = np.dot(np.dot(H, P_pred), H.T) + R  # Covarianza de la innovación
    K = np.dot(np.dot(P_pred, H.T), np.linalg.inv(S))  # Ganancia de Kalman

    # Actualización del estado y la covarian
