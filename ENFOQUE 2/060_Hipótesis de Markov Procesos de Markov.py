import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz de transición
P = np.array([[0.7, 0.3],  # Probabilidades de transición de A
              [0.4, 0.6]]) # Probabilidades de transición de B

# Definir los estados (A = 0, B = 1)
estados = ['A', 'B']

# Función para simular el proceso de Markov
def simular_markov(num_iteraciones=1000):
    # Estado inicial arbitrario (empezamos en A)
    estado_actual = 0  # A = 0, B = 1
    
    # Lista para almacenar la secuencia de estados
    secuencia_estados = []
    
    for _ in range(num_iteraciones):
        secuencia_estados.append(estados[estado_actual])
        
        # Elegir el siguiente estado basándose en la matriz de transición
        estado_actual = np.random.choice([0, 1], p=P[estado_actual])
    
    return secuencia_estados

# Simular el proceso de Markov
secuencia = simular_markov(1000)

# Mostrar la secuencia de estados generada
plt.plot(secuencia)
plt.title("Simulación de un Proceso de Markov (Estados A y B)")
plt.ylabel("Estado")
plt.yticks([0, 1], ['A', 'B'])
plt.xlabel("Iteraciones")
plt.show()
