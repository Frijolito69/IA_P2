import random
import math

# Función de activación: Sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivada de la Sigmoid (para backpropagation)
def derivada_sigmoid(x):
    sx = sigmoid(x)
    return sx * (1 - sx)

# Datos de entrenamiento (por ejemplo: XOR)
entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

salidas_deseadas = [0, 1, 1, 0]

# Configuración de la Red
# 2 entradas -> 2 neuronas en la capa oculta -> 1 salida
# Inicializar pesos y biases
pesos_entrada_oculta = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(2)]  # 2x2
bias_oculta = [random.uniform(-1, 1) for _ in range(2)]

pesos_oculta_salida = [random.uniform(-1, 1) for _ in range(2)]  # 2 conexiones ocultas -> salida
bias_salida = random.uniform(-1, 1)

# Tasa de aprendizaje
tasa_aprendizaje = 0.5

# Entrenar la red
for epoca in range(10000):
    error_total = 0
    for entrada, salida_real in zip(entradas, salidas_deseadas):
        ## Forward Pass

        # Capa oculta
        salida_oculta = []
        suma_oculta = []
        for i in range(2):
            suma = sum([entrada[j] * pesos_entrada_oculta[i][j] for j in range(2)]) + bias_oculta[i]
            suma_oculta.append(suma)
            salida_oculta.append(sigmoid(suma))

        # Capa de salida
        suma_salida = sum([salida_oculta[i] * pesos_oculta_salida[i] for i in range(2)]) + bias_salida
        salida_predicha = sigmoid(suma_salida)

        ## Calcular error
        error = salida_real - salida_predicha
        error_total += error ** 2

        ## Backward Pass (retropropagación)

        # Gradiente en la capa de salida
        gradiente_salida = derivada_sigmoid(suma_salida) * error

        # Gradientes en la capa oculta
        gradientes_oculta = []
        for i in range(2):
            gradiente = derivada_sigmoid(suma_oculta[i]) * gradiente_salida * pesos_oculta_salida[i]
            gradientes_oculta.append(gradiente)

        # Actualizar pesos oculta -> salida
        for i in range(2):
            pesos_oculta_salida[i] += tasa_aprendizaje * gradiente_salida * salida_oculta[i]
        bias_salida += tasa_aprendizaje * gradiente_salida

        # Actualizar pesos entrada -> oculta
        for i in range(2):
            for j in range(2):
                pesos_entrada_oculta[i][j] += tasa_aprendizaje * gradientes_oculta[i] * entrada[j]
            bias_oculta[i] += tasa_aprendizaje * gradientes_oculta[i]

    # Mostrar el error cada 1000 épocas
    if epoca % 1000 == 0:
        print(f"Época {epoca}, Error total: {error_total:.6f}")

# Probar la red entrenada
print("\nResultados finales:")
for entrada in entradas:
    # Capa oculta
    salida_oculta = []
    for i in range(2):
        suma = sum([entrada[j] * pesos_entrada_oculta[i][j] for j in range(2)]) + bias_oculta[i]
        salida_oculta.append(sigmoid(suma))
    
    # Capa de salida
    suma_salida = sum([salida_oculta[i] * pesos_oculta_salida[i] for i in range(2)]) + bias_salida
    salida_predicha = sigmoid(suma_salida)

    print(f"Entrada: {entrada}, Salida predicha: {salida_predicha:.4f}")
