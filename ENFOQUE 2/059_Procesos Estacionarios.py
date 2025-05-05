import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo AR(1)
phi = 0.8  # Coeficiente autorregresivo
sigma = 1  # Desviación estándar del ruido blanco
n = 1000    # Número de observaciones

# Inicialización
x = np.zeros(n)
epsilon = np.random.normal(0, sigma, n)  # Ruido blanco

# Generar el proceso AR(1)
for t in range(1, n):
    x[t] = phi * x[t-1] + epsilon[t]

# Graficar el proceso
plt.plot(x)
plt.title("Simulación de un Proceso AR(1) Estacionario")
plt.xlabel("Tiempo")
plt.ylabel("Valor de X_t")
plt.show()
