import heapq

# Definimos el grafo (diccionario de listas)
grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['Goal'],
    'E': ['Goal'],
    'Goal': []
}

# Definimos la heurística para cada nodo
heuristica = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 1,
    'E': 1,
    'Goal': 0
}

def busqueda_voraz(grafo, heuristica, inicio, objetivo):
    frontera = []  # Creamos la cola de prioridad (heap)
    heapq.heappush(frontera, (heuristica[inicio], [inicio]))  # Agregamos el nodo inicial
    visitados = set()  # Para marcar nodos ya explorados

    while frontera:
        _, ruta = heapq.heappop(frontera)  # Extraemos la ruta con menor heurística
        nodo_actual = ruta[-1]  # El último nodo de la ruta

        if nodo_actual == objetivo:  # Si encontramos el objetivo
            return ruta  # Devolvemos la ruta encontrada

        if nodo_actual not in visitados:  # Solo expandimos si no lo hemos visitado
            visitados.add(nodo_actual)  # Marcamos como visitado

            for vecino in grafo.get(nodo_actual, []):  # Expandimos los vecinos
                if vecino not in visitados:  # No agregar nodos ya visitados
                    nueva_ruta = list(ruta)  # Copiamos la ruta actual
                    nueva_ruta.append(vecino)  # Agregamos el vecino
                    heapq.heappush(frontera, (heuristica[vecino], nueva_ruta))  # Añadimos a la frontera

    return None  # Si no se encuentra camino

# Probamos la búsqueda
ruta = busqueda_voraz(grafo, heuristica, 'A', 'Goal')
print("Ruta encontrada con búsqueda voraz:", ruta)
