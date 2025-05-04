from collections import deque  # Importamos deque, que nos permite hacer una cola eficiente

# Definimos el grafo como un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(grafo, inicio, objetivo):
    cola = deque()  # Creamos una cola para ir guardando los nodos a visitar
    cola.append([inicio])  # Insertamos la ruta inicial que solo contiene el nodo de inicio

    while cola:
        ruta = cola.popleft()  # Sacamos la primera ruta de la cola
        nodo = ruta[-1]  # Tomamos el último nodo de la ruta

        if nodo == objetivo:  # Si encontramos el objetivo
            return ruta  # Devolvemos la ruta encontrada

        for vecino in grafo[nodo]:  # Recorremos los nodos vecinos
            nueva_ruta = list(ruta)  # Copiamos la ruta actual
            nueva_ruta.append(vecino)  # Agregamos el vecino a la nueva ruta
            cola.append(nueva_ruta)  # Agregamos la nueva ruta a la cola

    return None  # Si no se encuentra el objetivo, devolvemos None

# Probamos la función
ruta_encontrada = bfs(grafo, 'B', 'F')
print("Ruta encontrada (BFS):", ruta_encontrada)
