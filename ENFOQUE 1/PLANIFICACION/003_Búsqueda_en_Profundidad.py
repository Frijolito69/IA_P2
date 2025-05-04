# Definimos el grafo como un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(grafo, inicio, objetivo, ruta=None, visitados=None):
    if ruta is None:
        ruta = [inicio]  # Comenzamos la ruta con el nodo inicial
    if visitados is None:
        visitados = set()  # Creamos un conjunto para llevar registro de visitados

    visitados.add(inicio)  # Marcamos el nodo actual como visitado

    if inicio == objetivo:  # Si encontramos el objetivo
        return ruta  # Devolvemos la ruta encontrada

    for vecino in grafo[inicio]:  # Recorremos los vecinos del nodo actual
        if vecino not in visitados:  # Solo visitamos nodos no visitados
            nueva_ruta = list(ruta)  # Copiamos la ruta actual
            nueva_ruta.append(vecino)  # Agregamos el vecino a la nueva ruta
            resultado = dfs(grafo, vecino, objetivo, nueva_ruta, visitados)  # Llamada recursiva
            if resultado:  # Si encontramos una solución en la llamada recursiva
                return resultado

    return None  # Si no encontramos el objetivo, regresamos None

# Probamos la función
ruta_encontrada = dfs(grafo, 'A', 'F')
print("Ruta encontrada (DFS):", ruta_encontrada)
