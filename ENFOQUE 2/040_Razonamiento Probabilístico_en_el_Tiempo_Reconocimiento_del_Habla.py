import numpy as np

# Definimos los estados y observaciones
estados = ['a', 'b']
observaciones = ['X', 'Y']

# Probabilidades iniciales
prob_inicial = np.array([0.6, 0.4])

# Matriz de transición (de un estado al siguiente)
transicion = np.array([
    [0.7, 0.3],  # de 'a' a 'a', 'a' a 'b'
    [0.4, 0.6],  # de 'b' a 'a', 'b' a 'b'
])

# Matriz de emisión (probabilidad de observación dado estado)
emision = np.array([
    [0.9, 0.1],  # 'a' genera 'X', 'Y'
    [0.2, 0.8],  # 'b' genera 'X', 'Y'
])

# Observaciones reales captadas
secuencia_observaciones = ['X', 'Y']

# Algoritmo de Viterbi: encuentra la secuencia más probable
n_estados = len(estados)
n_observaciones = len(secuencia_observaciones)

# Matriz de probabilidades
V = np.zeros((n_observaciones, n_estados))

# Inicialización
V[0, :] = prob_inicial * emision[:, observaciones.index(secuencia_observaciones[0])]

# Recursión
for t in range(1, n_observaciones):
    for s in range(n_estados):
        V[t, s] = np.max(V[t-1] * transicion[:, s]) * emision[s, observaciones.index(secuencia_observaciones[t])]

# Resultado final
probabilidad_total = np.max(V[-1])
print(f"Probabilidad total de la mejor secuencia: {probabilidad_total}")
