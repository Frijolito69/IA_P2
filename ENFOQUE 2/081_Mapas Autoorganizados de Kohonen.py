import random
import math
import numpy as np

# Función de distancia Euclidiana
def euclidean_distance(x, w):
    return math.sqrt(sum([(xi - wi) ** 2 for xi, wi in zip(x, w)]))

# Función de vecindad (función Gaussiana)
def neighborhood_function(c, i, t, sigma_max, sigma_min):
    sigma = sigma_max * math.exp(-t / 1000) + sigma_min
    return math.exp(-euclidean_distance(c, i) ** 2 / (2 * sigma ** 2))

# Inicialización de pesos
def initialize_weights(grid_size, input_dim):
    return [[random.uniform(-1, 1) for _ in range(input_dim)] for _ in range(grid_size[0] * grid_size[1])]

# Función para encontrar la neurona ganadora
def winner_neuron(x, weights, grid_size):
    distances = [euclidean_distance(x, w) for w in weights]
    return distances.index(min(distances))

# Actualización de los pesos
def update_weights(weights, x, winner_idx, grid_size, t, sigma_max, sigma_min, learning_rate_max, learning_rate_min):
    # Encontrar la posición del ganador en la malla 2D
    winner_x = winner_idx % grid_size[1]
    winner_y = winner_idx // grid_size[1]
    
    # Actualización de los pesos
    for i, w in enumerate(weights):
        # Convertir la neurona al índice 2D
        i_x = i % grid_size[1]
        i_y = i // grid_size[1]
        
        # Función de vecindad
        h = neighborhood_function((winner_x, winner_y), (i_x, i_y), t, sigma_max, sigma_min)
        
        # Tasa de aprendizaje
        learning_rate = learning_rate_max * math.exp(-t / 1000) + learning_rate_min
        
        # Actualizar el peso
        weights[i] = [w_j + learning_rate * h * (x_j - w_j) for x_j, w_j in zip(x, w)]
    
    return weights

# Algoritmo SOM
def train_som(X, grid_size, input_dim, epochs=10000, sigma_max=1, sigma_min=0.1, learning_rate_max=0.1, learning_rate_min=0.01):
    # Inicializar pesos aleatorios
    weights = initialize_weights(grid_size, input_dim)
    
    # Entrenamiento
    for t in range(epochs):
        random.shuffle(X)  # Barajar las entradas
        for x in X:
            # Encontrar la neurona ganadora
            winner_idx = winner_neuron(x, weights, grid_size)
            
            # Actualizar los pesos
            weights = update_weights(weights, x, winner_idx, grid_size, t, sigma_max, sigma_min, learning_rate_max, learning_rate_min)
        
        if t % 1000 == 0:
            print(f"Epoch {t}/{epochs}")
    
    return weights

# Función para visualizar el mapa de Kohonen
def visualize_som(weights, grid_size):
    import matplotlib.pyplot as plt
    
    # Convertir los pesos a un formato adecuado para la visualización
    reshaped_weights = np.array(weights).reshape(grid_size[0], grid_size[1], -1)
    plt.imshow(reshaped_weights[:, :, 0], cmap='coolwarm', interpolation='nearest')
    plt.colorbar()
    plt.title("Mapa Autoorganizado de Kohonen")
    plt.show()

# Ejemplo de datos de entrada
X = [[random.random(), random.random()] for _ in range(100)]  # 100 puntos en 2D

# Parámetros
grid_size = (10, 10)  # Tamaño de la rejilla del mapa SOM
input_dim = 2  # Dimensión de los datos de entrada
epochs = 10000

# Entrenamiento del SOM
weights = train_som(X, grid_size, input_dim, epochs)

# Visualización del mapa entrenado
visualize_som(weights, grid_size)
