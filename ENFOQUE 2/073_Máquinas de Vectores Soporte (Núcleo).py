# Supongamos puntos muy sencillos
datos = [
    ([2, 3], 1),
    ([1, 1], -1),
    ([2, 1], -1),
    ([3, 3], 1),
]

# Parámetros del hiperplano
w = [0.0, 0.0]  # pesos
b = 0.0         # sesgo
learning_rate = 0.1
num_epocas = 10

# Función para predecir
def predict(x):
    suma = sum(w_i * x_i for w_i, x_i in zip(w, x)) + b
    return 1 if suma >= 0 else -1

# Entrenamiento muy básico
for epoca in range(num_epocas):
    for x, etiqueta_real in datos:
        prediccion = predict(x)
        if prediccion != etiqueta_real:
            # Actualizar pesos y sesgo
            for i in range(len(w)):
                w[i] += learning_rate * etiqueta_real * x[i]
            b += learning_rate * etiqueta_real

print(f"Pesos aprendidos: {w}")
print(f"Sesgo aprendido: {b}")

# Probamos con un nuevo dato
nuevo = [2, 2]
resultado = predict(nuevo)
print(f"El punto {nuevo} es clasificado como: {'Clase 1' if resultado == 1 else 'Clase -1'}")
