# Estados: 0, 1, 2
estados = [0, 1, 2]

# Acciones disponibles
acciones = ['izquierda', 'derecha']

# Función de transición (determinista)
def transicion(estado, accion):
    if accion == 'izquierda':
        return max(0, estado - 1)
    elif accion == 'derecha':
        return min(2, estado + 1)

# Función de recompensa
def recompensa(estado, accion, nuevo_estado):
    if nuevo_estado == 2:
        return 1
    else:
        return 0

# Factor de descuento
gamma = 0.9

# Inicializamos una política arbitraria: siempre moverse a la derecha
politica = {estado: 'derecha' for estado in estados}

# Inicializamos los valores en cero
valores = {estado: 0 for estado in estados}

# Parámetros
tolerancia = 0.001
convergencia = False
iteracion = 0

# Algoritmo de Iteración de Políticas
while not convergencia:
    iteracion += 1
    print(f"\n Iteración {iteracion}")

    # Paso 1: Evaluación de política
    cambio_maximo = float('inf')
    while cambio_maximo > tolerancia:
        cambio_maximo = 0
        nuevos_valores = valores.copy()
        
        for estado in estados:
            if estado == 2:
                continue  # Estado final
            
            accion = politica[estado]
            nuevo_estado = transicion(estado, accion)
            r = recompensa(estado, accion, nuevo_estado)
            v = r + gamma * valores[nuevo_estado]
            nuevos_valores[estado] = v
            
            cambio = abs(valores[estado] - v)
            if cambio > cambio_maximo:
                cambio_maximo = cambio
        
        valores = nuevos_valores
    
    print(f"Valores tras evaluación: {valores}")
    
    # Paso 2: Mejora de política
    politica_estable = True  # Suponemos que no cambia
    
    for estado in estados:
        if estado == 2:
            continue
        
        mejor_accion = None
        mejor_valor = float('-inf')
        
        for accion in acciones:
            nuevo_estado = transicion(estado, accion)
            r = recompensa(estado, accion, nuevo_estado)
            v = r + gamma * valores[nuevo_estado]
            
            if v > mejor_valor:
                mejor_valor = v
                mejor_accion = accion
        
        if mejor_accion != politica[estado]:
            politica_estable = False
            politica[estado] = mejor_accion
    
    print(f"Política actualizada: {politica}")

    if politica_estable:
        convergencia = True  # Terminamos si ya no cambia la política

# Resultado final
print("\n Política óptima encontrada:")
for estado in politica:
    print(f"Estado {estado}: {politica[estado]}")
