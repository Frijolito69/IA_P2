import numpy as np
import random
import matplotlib.pyplot as plt

# Parámetros
N = 1000  # Número de partículas
T = 50  # Número de pasos de tiempo
true_position = 0  # Posición verdadera inicial
velocity = 1  # Velocidad del objeto
std_process = 1  # Ruido del proceso (modelo de transición)
std_measurement = 2  # Ruido de la medición

# Inicialización de partículas
particles = np.random.normal(true_position, std_process, N)  # Partículas iniciales
weights = np.ones(N) / N  # Pesos iniciales

# Función de transición del sistema
def transition(x):
    return x + velocity + np.random.normal(0, std_process)

# Función de medición
def measurement(x):
    return x + np.random.normal(0, std_measurement)

# Inicialización de la lista para las estimaciones
estimates = []

# Filtro de partículas
for t in range(T):
    # 1. Predicción: Propagar las partículas
    particles = np.array([transition(p) for p in particles])
    
    # 2. Medición: Obtenemos una nueva observación
    z = measurement(true_position)
    
    # 3. Actualización de pesos: Usamos la diferencia entre la medición y el estado de las partículas
    weights = np.exp(-0.5 * ((particles - z) ** 2) / (std_measurement ** 2))
    weights /= sum(weights)  # Normalizamos los pesos
    
    # 4. Resampling: Re-muestrear según los pesos
    indices = np.random.choice(range(N), size=N, p=weights)
    particles = particles[indices]
    
    # Estimación de la posición (promedio de las partículas)
    estimate = np.mean(particles)
    estimates.append(estimate)

    # Actualizamos la posición verdadera para la siguiente iteración
    true_position += velocity

# Graficar resultados
plt.plot(estimates, label='Estimación del filtro de partículas')
plt.axhline(true_position, color='r', linestyle='--', label='Posición verdadera')
plt.legend()
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtrado de Partículas')
plt.show()
