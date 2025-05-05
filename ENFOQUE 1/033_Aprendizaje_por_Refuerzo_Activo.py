import random

# Definimos el entorno
estados = ['A', 'B', 'C', 'D', 'Meta']
acciones = ['ir_derecha', 'ir_izquierda']

# Definimos las transiciones
transiciones = {
    'A': {'ir_derecha': 'B', 'ir_izquierda': 'A'},
    'B': {'ir_derecha': 'C', 'ir_izquierda': 'A'},
    'C': {'ir_derecha': 'D', 'ir_izquierda': 'B'},
    'D': {'ir_derecha': 'Meta', 'ir_izquierda': 'C'},
    'Meta': {'ir_derecha': 'Meta', 'ir_izquierda': 'Meta'}
}

# Definimos las recompensas
recompensas = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'Meta': 10
}

# Inicializamos la Q-Table
Q = {}
for estado in estados:
    Q[estado] = {}
    for accion in acciones:
        Q[estado][accion] = 0  # Inicializamos con cero

# Parámetros
alpha = 0.1    # Tasa de aprendizaje
gamma = 0.9    # Factor de descuento
epsilon = 0.2  # Probabilidad de exploración
episodios = 1000

# Entrenamiento
for episodio in range(episodios):
    estado_actual = 'A'
    
    while estado_actual != 'Meta':
        # Selección de acción: exploración o explotación
        if random.uniform(0, 1) < epsilon:
            accion = random.choice(acciones)  # Explorar
        else:
            accion = max(Q[estado_actual], key=Q[estado_actual].get)  # Explotar
        
        # Ejecutar acción y observar nuevo estado y recompensa
        nuevo_estado = transiciones[estado_actual][accion]
        recompensa = recompensas[nuevo_estado]
        
        # Actualizar Q-Table usando la fórmula de Q-Learning
        Q[estado_actual][accion] = Q[estado_actual][accion] + alpha * (
            recompensa + gamma * max(Q[nuevo_estado].values()) - Q[estado_actual][accion]
        )
        
        # Moverse al nuevo estado
        estado_actual = nuevo_estado

# Mostrar la Q-Table aprendida
print("Tabla Q aprendida:")
for estado in Q:
    print(f"{estado}: {Q[estado]}")
