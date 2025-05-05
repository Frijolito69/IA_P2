import random

epsilon = 0.2  # Probabilidad de explorar

# Supongamos que tenemos estas acciones disponibles con estos Q-valores
acciones = ['ir_derecha', 'ir_izquierda']
Q_valores = {'ir_derecha': 7, 'ir_izquierda': 5}

# Decisión de exploración o explotación
if random.uniform(0, 1) < epsilon:
    # Exploración: elegir una acción aleatoria
    accion_elegida = random.choice(acciones)
else:
    # Explotación: elegir la mejor acción
    accion_elegida = max(Q_valores, key=Q_valores.get)

print(f"Acción elegida: {accion_elegida}")
