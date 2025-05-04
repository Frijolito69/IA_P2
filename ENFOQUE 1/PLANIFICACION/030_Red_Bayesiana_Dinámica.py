import random

# Definición de estados: 0 -> Reposo, 1 -> Movimiento
estados = ['Reposo', 'Movimiento']

# Probabilidades de transición
# P(Movimiento en t+1 | Movimiento en t)
P_movimiento = 0.8
# P(Movimiento en t+1 | Reposo en t)
P_reposo = 0.2

# Probabilidades de observación
# P(Sensor detecta movimiento | Movimiento)
P_observacion = 0.9
# P(Sensor no detecta movimiento | Movimiento)
P_no_observacion = 0.1

# Función de transición de estado (movimiento o reposo)
def transicion_estado(estado_actual):
    if estado_actual == 'Movimiento':
        return 'Movimiento' if random.random() < P_movimiento else 'Reposo'
    else:  # Estado actual: Reposo
        return 'Movimiento' if random.random() < P_reposo else 'Reposo'

# Función de observación
def observacion(estado):
    if estado == 'Movimiento':
        return 'Movimiento' if random.random() < P_observacion else 'Reposo'
    else:
        return 'Reposo' if random.random() < P_no_observacion else 'Movimiento'

# Simulación de la red bayesiana dinámica a lo largo de 5 pasos de tiempo
estado_actual = 'Reposo'  # El robot comienza en reposo
for t in range(5):
    print(f"Paso {t + 1}:")
    print(f"  Estado real: {estado_actual}")
    
    # El robot toma una acción y su estado cambia
    estado_actual = transicion_estado(estado_actual)
    
    # Observación del sensor (posible error)
    observacion_actual = observacion(estado_actual)
    print(f"  Observación del sensor: {observacion_actual}")
    
    print("---")
