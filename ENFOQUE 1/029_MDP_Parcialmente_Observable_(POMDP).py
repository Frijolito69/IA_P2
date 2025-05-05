import random

# Definición de los estados, acciones y observaciones
estados = ['S0', 'S1', 'S2']  # Tres posibles estados
acciones = ['derecha', 'izquierda']
observaciones = ['sensor_cerca', 'sensor_lejos']

# Probabilidades de transición de estados
def transicion(estado, accion):
    if accion == 'derecha':
        return estados[min(estados.index(estado) + 1, 2)]  # No puede ir más allá de S2
    elif accion == 'izquierda':
        return estados[max(estados.index(estado) - 1, 0)]  # No puede ir antes de S0

# Función de recompensa
def recompensa(estado):
    if estado == 'S2':
        return 10  # Recompensa cuando llega al objetivo
    else:
        return -1  # Penalización en otros estados

# Función de observación (sensor ruidoso)
def observacion(estado):
    if estado == 'S2':
        return random.choices(observaciones, [0.9, 0.1])[0]  # Más probable que el sensor diga 'sensor_cerca'
    else:
        return random.choices(observaciones, [0.5, 0.5])[0]  # Sensor más ruidoso

# Inicialización
estado_real = 'S0'
estado_estimado = 'S0'  # El agente comienza sin saber su ubicación exacta
total_recompensa = 0

# Simulación del POMDP
print("🚀 Comenzando simulación:")
for i in range(10):  # Simulamos 10 pasos
    # El agente observa el entorno (sensor ruidoso)
    obs = observacion(estado_real)
    print(f"\nIteración {i + 1} - Estado estimado: {estado_estimado} | Observación: {obs}")

    # El agente decide moverse a la derecha
    accion = 'derecha'
    estado_real = transicion(estado_real, accion)
    recompensa_actual = recompensa(estado_real)
    
    # Estima su estado (aquí solo se asume que ajusta su creencia)
    if obs == 'sensor_cerca':
        estado_estimado = 'S2'  # Si el sensor indica que está cerca, el agente asume que está en S2
    else:
        estado_estimado = estado_real  # Caso más conservador, el agente asume que está en el estado real

    total_recompensa += recompensa_actual
    print(f"Acción: {accion} | Nuevo estado: {estado_real} | Recompensa: {recompensa_actual}")

print(f"\n✅ Recompensa total acumulada: {total_recompensa}")
