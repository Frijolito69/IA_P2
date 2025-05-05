import random
import math

# Función de activación Sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivada de Sigmoid
def sigmoid_derivada(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Datos de entrenamiento (XOR sencillo)
datos = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

# Inicializar pesos y sesgos aleatoriamente
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)
b = random.uniform(-1, 1)

# Hiperparámetros
learning_rate = 0.5
num_epocas = 10000

# Entrenamiento
for epoca in range(num_epocas):
    for entrada, salida_esperada in datos:
        x1, x2 = entrada
        
        # Propagación hacia adelante
        suma = w1 * x1 + w2 * x2 + b
        salida = sigmoid(suma)
        
        # Calcular error
        error = salida_esperada - salida
        
        # Derivadas para ajustar
        delta = error * sigmoid_derivada(suma)
        
        # Actualizar pesos y sesgo
        w1 += learning_rate * delta * x1
        w2 += learning_rate * delta * x2
        b += learning_rate * delta

# Mostrar pesos finales
print(f"Pesos finales: w1 = {w1:.2f}, w2 = {w2:.2f}, b = {b:.2f}")

# Probar la red
for entrada, salida_real in datos:
    x1, x2 = entrada
    salida = sigmoid(w1 * x1 + w2 * x2 + b)
    prediccion = round(salida)
    print(f"Entrada: {entrada}, Predicción: {prediccion}, Real: {salida_real}")
