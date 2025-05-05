import random

# Definimos los estados y acciones
estados = ['A', 'B', 'C', 'D', 'Meta']
acciones = ['ir_derecha', 'ir_izquierda']

# Definimos las transiciones entre estados
transiciones = {
    'A': {'ir_derecha': 'B', 'ir_izquierda': 'A'},
    'B': {'ir_derecha': 'C', 'ir_izquierda': 'A'},
    'C': {'ir_derecha': 'D', 'ir_izquierda': 'B'},
    'D': {'ir_derecha': 'Meta', 'ir_izquierda': 'C'},
    'Meta': {'ir_derecha': 'Meta', 'ir_izquierda': 'Meta'}
}

# Recompensas para cada estado
recompensas = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'Meta': 10  # El objetivo es alcanzar Meta
}

# Inicializamos la Q-Table con valores 0
Q = {}
for estado in estados:
    Q[estado] = {}
    for accion in acciones:
        Q[estado][accion] = 0  # Todos los Q-valores iniciales son 0

# Parámetros
alpha = 0.1    # Tasa de aprendizaje
gamma = 0.9    # Factor de descuento
epsilon = 0.2  # Probabilidad de exploración
episodios = 1000  # Número de veces que se entrena

# Entrenamiento
for episodio in range(episodios):
    estado_actual = 'A'  # Siempre comenzamos desde 'A'
    
    while estado_actual != 'Meta':
        # Escogemos una acción: exploramos o explotamos
        if random.uniform(0, 1) < epsilon:
            accion = random.choice(acciones)  # Exploramos
        else:
            accion = max(Q[estado_actual], key=Q[estado_actual].get)  # Explotamos mejor acción
        
        # Ejecutamos acción y obtenemos nuevo estado y recompensa
        nuevo_estado = transiciones[estado_actual][accion]
        recompensa = recompensas[nuevo_estado]
        
        # Actualizamos la Q-Table
        Q[estado_actual][accion] = Q[estado_actual][accion] + alpha * (
            recompensa + gamma * max(Q[nuevo_estado].values()) - Q[estado_actual][accion]
        )
        
        # Avanzamos al nuevo estado
        estado_actual = nuevo_estado

# Imprimimos la tabla Q aprendida
print("Tabla Q aprendida:")
for estado in Q:
    print(f"{estado}: {Q[estado]}")
