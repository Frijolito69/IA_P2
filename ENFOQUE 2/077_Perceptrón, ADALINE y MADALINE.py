# Perceptrón: Clasificación binaria
import math

# Función de activación (signo)
def activacion(x):
    return 1 if x >= 0 else 0

# Datos de entrada (x1, x2) y etiquetas (deseado)
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
etiquetas = [0, 0, 0, 1]  # El resultado deseado es el AND lógico

# Inicialización de pesos y sesgo
pesos = [0.0, 0.0]
sesgo = 0.0
tasa_aprendizaje = 0.1
errores = []

# Entrenamiento del perceptrón
for epoca in range(10):
    error_total = 0
    for x, d in zip(entradas, etiquetas):
        # Calculamos la salida del perceptrón
        suma_ponderada = sum(xi * wi for xi, wi in zip(x, pesos)) + sesgo
        salida = activacion(suma_ponderada)
        
        # Calculamos el error
        error = d - salida
        error_total += abs(error)
        
        # Actualización de pesos y sesgo
        pesos = [wi + tasa_aprendizaje * error * xi for wi, xi in zip(pesos, x)]
        sesgo += tasa_aprendizaje * error
        
    errores.append(error_total)

# Mostramos los resultados finales
print(f"Pesos finales: {pesos}")
print(f"Sesgo final: {sesgo}")
print(f"Errores por época: {errores}")
