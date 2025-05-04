# Definimos el grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dls(grafo, inicio, objetivo, limite, ruta=None, visitados=None):
    if ruta is None:
        ruta = [inicio]  # Comenzamos la ruta con el nodo inicial
    if visitados is None:
        visitados = set()  # Creamos un conjunto para nodos visitados

    visitados.add(inicio)  # Marcamos el nodo actual como visitado

    if inicio == objetivo:  # Si llegamos al objetivo
        return ruta  # Retornamos la ruta encontrada

    if limite <= 0:  # Si ya alcanzamos el límite de profundidad
        return None  # No seguimos explorando más

    for vecino in grafo[inicio]:  # Recorremos los vecinos
        if vecino not in visitados:  # Solo visitamos no visitados
            nueva_ruta = list(ruta)  # Copiamos la ruta actual
            nueva_ruta.append(vecino)  # Agregamos el vecino
            resultado = dls(grafo, vecino, objetivo, limite-1, nueva_ruta, visitados)  # Bajamos el límite en 1
            if resultado:  # Si encontramos una solución
                return resultado

    return None  # Si no encontramos solución desde este nodo

# Probamos la función
limite = 3  # Definimos el límite de profundidad
ruta_encontrada = dls(grafo, 'A', 'F', limite)
print(f"Ruta encontrada (DLS con límite {limite}):", ruta_encontrada)
