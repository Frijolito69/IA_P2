import heapq

# Definimos el grafo con costos reales entre nodos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('E', 1)],
    'D': [('Goal', 5)],
    'E': [('Goal', 1)],
    'Goal': []
}

# Definimos la heurística para cada nodo
heuristica = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 4,
    'E': 1,
    'Goal': 0
}

def busqueda_A_estrella(grafo, heuristica, inicio, objetivo):
    frontera = []  # Cola de prioridad basada en f(n)
    heapq.heappush(frontera, (heuristica[inicio], 0, [inicio]))  # (f(n), g(n), ruta)

    visitados = set()  # Para evitar ciclos

    while frontera:
        f_actual, g_actual, ruta = heapq.heappop(frontera)
        nodo_actual = ruta[-1]

        if nodo_actual == objetivo:
            return ruta

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino, costo in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    g_nuevo = g_actual + costo  # Nuevo costo real
                    f_nuevo = g_nuevo + heuristica[vecino]  # f(n) = g(n) + h(n)
                    nueva_ruta = list(ruta)
                    nueva_ruta.append(vecino)
                    heapq.heappush(frontera, (f_nuevo, g_nuevo, nueva_ruta))

    return None

# Prueba
ruta = busqueda_A_estrella(grafo, heuristica, 'A', 'Goal')
print("Ruta encontrada con A*:", ruta)
