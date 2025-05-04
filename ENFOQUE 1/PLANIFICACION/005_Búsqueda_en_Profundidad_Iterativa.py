# Definimos el grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Función de búsqueda en profundidad limitada (DLS), igual que la anterior
def dls(grafo, inicio, objetivo, limite, ruta=None, visitados=None):
    if ruta is None:
        ruta = [inicio]  # Empezamos la ruta
    if visitados is None:
        visitados = set()  # Creamos el conjunto de visitados

    visitados.add(inicio)  # Marcamos el nodo como visitado

    if inicio == objetivo:  # Si encontramos el objetivo
        return ruta  # Devolvemos la ruta

    if limite <= 0:  # Si alcanzamos el límite
        return None

    for vecino in grafo[inicio]:  # Exploramos los vecinos
        if vecino not in visitados:
            nueva_ruta = list(ruta)  # Copiamos la ruta
            nueva_ruta.append(vecino)  # Agregamos el vecino
            resultado = dls(grafo, vecino, objetivo, limite-1, nueva_ruta, visitados)  # Búsqueda recursiva con límite-1
            if resultado:
                return resultado

    return None  # No se encontró el objetivo en este camino

# Función principal de IDS
def ids(grafo, inicio, objetivo, limite_maximo):
    for limite in range(limite_maximo + 1):  # Iteramos desde 0 hasta el límite máximo
        print(f"Buscando con límite de profundidad: {limite}")
        ruta_encontrada = dls(grafo, inicio, objetivo, limite)  # Ejecutamos DLS con el límite actual
        if ruta_encontrada:  # Si encontramos la solución
            return ruta_encontrada  # Devolvemos la ruta

    return None  # Si no encontramos después de todos los límites

# Probamos la función
limite_maximo = 5  # Límite máximo hasta donde queremos buscar
ruta = ids(grafo, 'A', 'F', limite_maximo)
print("Ruta encontrada (IDS):", ruta)
