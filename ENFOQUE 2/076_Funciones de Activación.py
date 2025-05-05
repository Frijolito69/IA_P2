import math

# Función Sigmoide
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Probar con algunos valores
valores = [-5, -1, 0, 1, 5]

for valor in valores:
    salida = sigmoid(valor)
    print(f"sigmoid({valor}) = {salida:.4f}")
