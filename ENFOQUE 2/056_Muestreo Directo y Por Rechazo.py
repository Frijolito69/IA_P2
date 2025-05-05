import random
import math

# Función de densidad de la distribución normal estándar
def p(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x**2)

# Función de densidad de la distribución propuesta (uniforme)
def q(x):
    if -5 <= x <= 5:
        return 1 / 10  # Uniforme en el intervalo [-5, 5]
    else:
        return 0

# Muestreo por Rechazo
def muestreo_por_rechazo():
    # 1. Muestro de la distribución uniforme entre -5 y 5
    x_star = random.uniform(-5, 5)
    
    # 2. Calculamos M, el factor de escala
    M = math.sqrt(2 * math.pi) * 10  # M mayor o igual que el cociente de las densidades

    # 3. Generamos un número aleatorio
    u = random.uniform(0, 1)
    
    # 4. Aceptamos o rechazamos la muestra
    if u <= p(x_star) / (M * q(x_star)):
        return x_star
    else:
        return muestreo_por_rechazo()  # Reintentar si es rechazada

# Generamos 5 muestras usando el muestreo por rechazo
muestras_rechazo = [muestreo_por_rechazo() for _ in range(5)]
print("Muestras por Rechazo (Normal Estándar):", muestras_rechazo)
