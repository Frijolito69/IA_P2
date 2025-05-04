import heapq

# Definimos un grafo donde los nodos son conectados
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Definimos una heurística para cada nodo (valores estimados al objetivo)
heuristica = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0  # El objetivo tiene heurística 0
}

def busqueda_heuristica(grafo, heuristica, inicio, objetivo):
    frontera = []  # Usamos un heap (cola de prioridad)
    heapq.heappush(frontera, (heuristica[inicio], [inicio]))  # (heurística, ruta)

    visitados = set()  # Para no visitar dos veces

    while frontera:
        _, ruta = heapq.heappop(frontera)  # Tomamos la ruta de menor heurística
        nodo_actual = ruta[-1]

        if nodo_actual == objetivo:
            return ruta

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    nueva_ruta = list(ruta)
                    nueva_ruta.append(vecino)
                    heapq.heappush(frontera, (heuristica[vecino], nueva_ruta))

    return None

# Probamos
ruta = busqueda_heuristica(grafo, heuristica, 'B', 'F')
print("Ruta encontrada usando heurística:", ruta)
