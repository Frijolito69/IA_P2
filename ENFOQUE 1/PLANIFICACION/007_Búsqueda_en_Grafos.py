from collections import deque

# Definimos un grafo con ciclos
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'A'],  # ciclo hacia 'A'
    'D': [],
    'E': ['F'],
    'F': []
}

def busqueda_en_grafos_bfs(grafo, inicio, objetivo):
    frontera = deque([[inicio]])  # Usamos una cola para mantener rutas
    visitados = set()  # Usamos un conjunto para nodos visitados

    while frontera:
        ruta = frontera.popleft()  # Sacamos la primera ruta de la cola
        nodo_actual = ruta[-1]  # El nodo actual es el último de la ruta

        if nodo_actual == objetivo:  # Si encontramos el objetivo
            return ruta  # Retornamos la ruta completa

        if nodo_actual not in visitados:  # Solo exploramos nodos no visitados
            visitados.add(nodo_actual)  # Marcamos como visitado

            for vecino in grafo.get(nodo_actual, []):  # Expandimos los vecinos
                nueva_ruta = list(ruta)  # Copiamos la ruta actual
                nueva_ruta.append(vecino)  # Agregamos el vecino a la ruta
                frontera.append(nueva_ruta)  # Agregamos la nueva ruta a la frontera

    return None  # Si no encontramos el objetivo

# Probamos la función
ruta = busqueda_en_grafos_bfs(grafo, 'A', 'F')
print("Ruta encontrada (Búsqueda en Grafos BFS):", ruta)
