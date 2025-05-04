class Nodo:
    def __init__(self, nombre, hijos=None, es_and=False):
        self.nombre = nombre
        self.hijos = hijos or []
        self.es_and = es_and  # True si es un nodo AND

def busqueda_AO_estrella(nodo, heuristica):
    if not nodo.hijos:  # Si no hay hijos, ya estamos en el objetivo
        return [nodo.nombre], heuristica.get(nodo.nombre, 0)

    mejor_solucion = None
    mejor_costo = float('inf')

    if nodo.es_and:
        solucion_total = []
        costo_total = 0
        for hijo in nodo.hijos:
            solucion, costo = busqueda_AO_estrella(hijo, heuristica)
            solucion_total += solucion
            costo_total += costo
        return [nodo.nombre] + solucion_total, costo_total
    else:
        for hijo in nodo.hijos:
            solucion, costo = busqueda_AO_estrella(hijo, heuristica)
            if costo < mejor_costo:
                mejor_solucion = solucion
                mejor_costo = costo
        return [nodo.nombre] + mejor_solucion, mejor_costo

# Definimos nodos
D = Nodo('D')
E = Nodo('E')
F = Nodo('F')

B = Nodo('B', hijos=[D, E], es_and=True)
C = Nodo('C', hijos=[F])

A = Nodo('A', hijos=[B, C])

# Heurística
heuristica = {
    'D': 2,
    'E': 2,
    'F': 3,
    'B': 4,
    'C': 3,
    'A': 5
}

# Ejecutamos AO*
ruta, costo = busqueda_AO_estrella(A, heuristica)
print("Ruta encontrada con AO*:", ruta)
print("Costo total:", costo)
