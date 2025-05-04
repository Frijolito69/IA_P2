import numpy as np

# Definir las habitaciones y las recompensas
estados = [1, 2, 3]  # Habitaciones 1, 2, 3
recompensas = {1: 0, 2: 1, 3: 2}

# Simular un episodio de aprendizaje (secuencia de habitaciones visitadas)
# El agente comienza en la habitación 1
episodio = [1, 2, 3, 2, 1]  # Episodio de ejemplo (secuencia de estados)

# Método de Monte Carlo para estimar los valores de los estados
# Inicialización
valores = {estado: 0 for estado in estados}
count = {estado: 0 for estado in estados}

# Algoritmo de Monte Carlo
for t in range(len(episodio)):
    estado = episodio[t]
    # Acumular la recompensa en el estado
    valores[estado] += sum([recompensas[s] for s in episodio[t:]])  # Recompensa futura
    count[estado] += 1

# Estimar el valor de cada estado
for estado in estados:
    valores[estado] /= count[estado]

# Mostrar los valores estimados
print("Valores estimados de los estados:")
for estado, valor in valores.items():
    print(f"Estado {estado}: Valor estimado = {valor:.2f}")
