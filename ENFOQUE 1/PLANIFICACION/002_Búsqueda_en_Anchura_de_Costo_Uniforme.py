import heapq  # Importamos heapq para usar una cola de prioridad (mínimo primero)

# Definimos el grafo, pero ahora con costos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def ucs(grafo, inicio, objetivo):
    cola = []  # Creamos una lista para la cola de prioridad
    heapq.heappush(cola, (0, [inicio]))  # Insertamos una tupla (costo acumulado, ruta)

    while cola:
        costo_actual, ruta = heapq.heappop(cola)  # Sacamos la ruta con menor costo
        nodo = ruta[-1]  # El último nodo de la ruta actual

        if nodo == objetivo:  # Si llegamos al objetivo
            return ruta, costo_actual  # Devolvemos la ruta y el costo

        for vecino, costo in grafo[nodo]:  # Recorremos vecinos y sus costos
            nueva_ruta = list(ruta)  # Copiamos la ruta actual
            nueva_ruta.append(vecino)  # Añadimos el vecino a la ruta
            nuevo_costo = costo_actual + costo  # Sumamos el costo
            heapq.heappush(cola, (nuevo_costo, nueva_ruta))  # Insertamos en la cola

    return None, None  # Si no hay camino al objetivo

# Probamos la función
ruta_encontrada, costo_total = ucs(grafo, 'A', 'F')
print("Ruta encontrada (UCS):", ruta_encontrada)
print("Costo total:", costo_total)
