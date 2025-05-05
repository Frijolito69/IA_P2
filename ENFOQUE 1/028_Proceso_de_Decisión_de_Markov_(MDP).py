import random

# Estados: 0 (inicio), 1, 2 (meta)
estados = [0, 1, 2]

# Acciones posibles
acciones = ['derecha', 'izquierda']

# Definimos la transición: (estado actual, acción) -> estado siguiente
def transicion(estado, accion):
    if accion == 'derecha':
        if estado < 2:
            return estado + 1
    elif accion == 'izquierda':
        if estado > 0:
            return estado - 1
    return estado  # Si no puede moverse, se queda

# Función de recompensa
def recompensa(estado, accion, nuevo_estado):
    if nuevo_estado == 2:
        return 10  # Llegar a la meta da 10 puntos
    else:
        return -1  # Cada paso cuesta energía (-1)

# Política simple: siempre intenta ir a la derecha
politica = {0: 'derecha', 1: 'derecha', 2: None}

# Simulación de la ejecución del MDP
estado_actual = 0
total_recompensa = 0

print("🚀 Comenzando simulación:")

while estado_actual != 2:
    accion = politica[estado_actual]
    nuevo_estado = transicion(estado_actual, accion)
    r = recompensa(estado_actual, accion, nuevo_estado)
    print(f"Estado {estado_actual} --{accion}--> {nuevo_estado} | Recompensa: {r}")
    
    total_recompensa += r
    estado_actual = nuevo_estado

print(f"\n Recompensa total acumulada: {total_recompensa}")
