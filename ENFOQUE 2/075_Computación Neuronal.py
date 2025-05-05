import math

# Función de activación: Sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Datos de ejemplo
entradas = [0.5, -0.2, 0.1]  # x1, x2, x3
pesos = [0.4, 0.7, -0.5]     # w1, w2, w3
sesgo = 0.1

# Calcular la suma ponderada
suma = 0
for x, w in zip(entradas, pesos):
    suma += x * w
suma += sesgo  # Añadir el sesgo

# Aplicar función de activación
salida = sigmoid(suma)

# Mostrar el resultado
print(f"La salida de la neurona es: {salida:.4f}")
