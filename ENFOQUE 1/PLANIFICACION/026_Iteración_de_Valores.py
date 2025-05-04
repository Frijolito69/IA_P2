# Estados: 0, 1, 2
estados = [0, 1, 2]

# Acciones: izquierda y derecha
acciones = ['izquierda', 'derecha']

# Definimos transiciones deterministas
def transicion(estado, accion):
    if accion == 'izquierda':
        return max(0, estado - 1)  # No puede ir más a la izquierda de 0
    elif accion == 'derecha':
        return min(2, estado + 1)  # No puede ir más a la derecha de 2

# Definimos recompensas
def recompensa(estado, accion, nuevo_estado):
    if nuevo_estado == 2:
        return 1  # Solo llegar al estado 2 da recompensa
    else:
        return 0

# Factor de descuento
gamma = 0.9

# Inicializamos valores de los estados en 0
valores = {estado: 0 for estado in estados}

# Parámetros de la iteración
tolerancia = 0.001  # Criterio de convergencia
cambio_maximo = float('inf')  # Para controlar el cambio máximo en cada iteración
iteracion = 0

# Algoritmo de Iteración de Valores
while cambio_maximo > tolerancia:
    cambio_maximo = 0
    nuevos_valores = valores.copy()
    
    for estado in estados:
        if estado == 2:
            continue  # Estado final, no actualizar
        
        valores_acciones = []
        
        for accion in acciones:
            nuevo_estado = transicion(estado, accion)
            r = recompensa(estado, accion, nuevo_estado)
            v = r + gamma * valores[nuevo_estado]
            valores_acciones.append(v)
        
        mejor_valor = max(valores_acciones)
        nuevos_valores[estado] = mejor_valor
        
        # Actualizamos el máximo cambio
        cambio = abs(valores[estado] - mejor_valor)
        if cambio > cambio_maximo:
            cambio_maximo = cambio

    valores = nuevos_valores
    iteracion += 1
    print(f"Iteración {iteracion}: {valores}")

# Al terminar, derivamos la mejor política
politica = {}

for estado in estados:
    if estado == 2:
        politica[estado] = None  # Estado terminal
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
    
    politica[estado] = mejor_accion

print("\n Política óptima encontrada:")
for estado in politica:
    print(f"Estado {estado}: {politica[estado]}")
