from collections import deque

# Definimos el grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bidirectional_search(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]

    # Inicializamos dos colas: una para el inicio y otra para el objetivo
    frontera_inicio = deque([[inicio]])
    frontera_objetivo = deque([[objetivo]])

    # Conjuntos para guardar nodos visitados en cada dirección
    visitados_inicio = {inicio}
    visitados_objetivo = {objetivo}

    while frontera_inicio and frontera_objetivo:
        # Expandimos desde el inicio
        ruta_inicio = frontera_inicio.popleft()
        nodo_inicio = ruta_inicio[-1]

        for vecino in grafo.get(nodo_inicio, []):
            if vecino not in visitados_inicio:
                nueva_ruta = list(ruta_inicio)
                nueva_ruta.append(vecino)
                frontera_inicio.append(nueva_ruta)
                visitados_inicio.add(vecino)

                if vecino in visitados_objetivo:
                    # Se encuentran las búsquedas
                    ruta_objetivo = encontrar_ruta_objetivo(frontera_objetivo, vecino)
                    if ruta_objetivo:
                        ruta_objetivo.pop(0)  # Evitamos repetir el nodo de encuentro
                        return nueva_ruta + ruta_objetivo[::-1]  # Unimos ambas rutas

        # Expandimos desde el objetivo
        ruta_objetivo = frontera_objetivo.popleft()
        nodo_objetivo = ruta_objetivo[-1]

        for vecino in grafo.get(nodo_objetivo, []):
            if vecino not in visitados_objetivo:
                nueva_ruta = list(ruta_objetivo)
                nueva_ruta.append(vecino)
                frontera_objetivo.append(nueva_ruta)
                visitados_objetivo.add(vecino)

                if vecino in visitados_inicio:
                    # Se encuentran las búsquedas
                    ruta_inicio = encontrar_ruta_inicio(frontera_inicio, vecino)
                    if ruta_inicio:
                        ruta_inicio.pop(0)  # Evitamos repetir el nodo de encuentro
                        return ruta_inicio + nueva_ruta[::-1]  # Unimos ambas rutas

    return None  # Si no encontramos un camino

def encontrar_ruta_objetivo(frontera_objetivo, nodo_encontrado):
    for ruta in frontera_objetivo:
        if ruta[-1] == nodo_encontrado:
            return ruta
    return None

def encontrar_ruta_inicio(frontera_inicio, nodo_encontrado):
    for ruta in frontera_inicio:
        if ruta[-1] == nodo_encontrado:
            return ruta
    return None

# Probamos la función
ruta = bidirectional_search(grafo, 'A', 'F')
print("Ruta encontrada (Bidireccional):", ruta)
