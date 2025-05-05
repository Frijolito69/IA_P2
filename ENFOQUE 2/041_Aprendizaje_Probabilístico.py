import random
import math

# Activación Sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivada de la Sigmoid (para backpropagation)
def derivada_sigmoid(x):
    sx = sigmoid(x)
    return sx * (1 - sx)

# Datos de entrada (XOR simplificado)
entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Etiquetas de salida (queremos que aprenda XOR)
salidas_deseadas = [0, 1, 1, 0]

# Inicializar pesos aleatoriamente
peso_entrada_1 = random.uniform(-1, 1)
peso_entrada_2 = random.uniform(-1, 1)
bias = random.uniform(-1, 1)  # Umbral

# Tasa de aprendizaje
tasa_aprendizaje = 0.5

# Entrenar por varias épocas
for epoca in range(10000):
    error_total = 0
    for entrada, salida_real in zip(entradas, salidas_deseadas):
        # Propagación hacia adelante
        suma_ponderada = (entrada[0] * peso_entrada_1) + (entrada[1] * peso_entrada_2) + bias
        salida_predicha = sigmoid(suma_ponderada)

        # Calcular el error
        error = salida_real - salida_predicha
        error_total += error ** 2  # error cuadrático acumulado

        # Ajustar pesos (backpropagation manual)
        gradiente = derivada_sigmoid(suma_ponderada)
        peso_entrada_1 += tasa_aprendizaje * error * gradiente * entrada[0]
        peso_entrada_2 += tasa_aprendizaje * error * gradiente * entrada[1]
        bias += tasa_aprendizaje * error * gradiente  # actualizar el bias también

    # Mostrar el error cada 1000 épocas
    if epoca % 1000 == 0:
        print(f"Época {epoca}, Error total: {error_total}")

# Probar la red entrenada
print("\nResultados finales:")
for entrada in entradas:
    suma_ponderada = (entrada[0] * peso_entrada_1) + (entrada[1] * peso_entrada_2) + bias
    salida_predicha = sigmoid(suma_ponderada)
    print(f"Entrada: {entrada}, Salida predicha: {salida_predicha:.4f}")
