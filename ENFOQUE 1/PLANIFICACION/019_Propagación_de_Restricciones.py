from collections import deque

# Variables
variables = ['A', 'B', 'C', 'D']

# Dominios
dominios = {
    'A': ['rojo', 'verde', 'azul'],
    'B': ['rojo', 'verde', 'azul'],
    'C': ['rojo', 'verde', 'azul'],
    'D': ['rojo', 'verde', 'azul'],
}

# Vecinos
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Función que elimina valores inconsistentes
def eliminar_inconsistentes(xi, xj):
    eliminado = False
    for x in dominios[xi][:]:  # Revisamos copia del dominio
        # Si no hay ningún valor en xj compatible con x, eliminamos x
        if not any(x != y for y in dominios[xj]):
            dominios[xi].remove(x)
            eliminado = True
    return eliminado

# Algoritmo AC-3
def ac3():
    # Creamos una cola de todos los arcos
    cola = deque()
    for var in variables:
        for vecino in vecinos[var]:
            cola.append((var, vecino))
    
    # Procesamos la cola
    while cola:
        (xi, xj) = cola.popleft()
        if eliminar_inconsistentes(xi, xj):
            if not dominios[xi]:
                return False  # Sin solución posible
            # Agregamos todos los vecinos de xi de nuevo a la cola
            for xk in vecinos[xi]:
                if xk != xj:
                    cola.append((xk, xi))
    return True

# Ejecutamos AC-3
resultado = ac3()

# Mostramos los dominios después de AC-3
if resultado:
    print("Dominios después de aplicar AC-3:")
    for var in variables:
        print(f"{var}: {dominios[var]}")
else:
    print("No se encontró solución, dominio vacío.")
