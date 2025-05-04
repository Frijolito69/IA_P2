import numpy as np

# Definimos los estados y acciones
estados = ['A', 'B']
acciones = ['ir_derecha', 'ir_izquierda']

# Inicializamos la política de forma estocástica (probabilidades)
# [P(ir_derecha), P(ir_izquierda)] para cada estado
politica = {
    'A': np.array([0.5, 0.5]),
    'B': np.array([0.5, 0.5])
}

# Definimos las recompensas manualmente
recompensas = {
    ('A', 'ir_derecha'): 1,
    ('A', 'ir_izquierda'): 0,
    ('B', 'ir_derecha'): 2,
    ('B', 'ir_izquierda'): -1
}

# Parámetros
tasa_aprendizaje = 0.1
episodios = 1000

# Entrenamiento
for episodio in range(episodios):
    estado = np.random.choice(estados)  # Comienza en A o B aleatoriamente
    
    # Elegimos acción según la política actual (probabilísticamente)
    accion = np.random.choice(acciones, p=politica[estado])
    
    # Recibimos recompensa basada en estado y acción
    recompensa = recompensas[(estado, accion)]
    
    # Calculamos gradiente (actualización simple basada en REINFORCE)
    if accion == 'ir_derecha':
        politica[estado][0] += tasa_aprendizaje * recompensa
        politica[estado][1] -= tasa_aprendizaje * recompensa
    else:
        politica[estado][0] -= tasa_aprendizaje * recompensa
        politica[estado][1] += tasa_aprendizaje * recompensa
    
    # Normalizamos para que siga siendo una probabilidad válida
    politica[estado] = np.clip(politica[estado], 0.01, 0.99)
    politica[estado] /= np.sum(politica[estado])

# Mostrar política aprendida
print("Política aprendida:")
for estado in politica:
    print(f"En estado {estado}: {politica[estado]}")
