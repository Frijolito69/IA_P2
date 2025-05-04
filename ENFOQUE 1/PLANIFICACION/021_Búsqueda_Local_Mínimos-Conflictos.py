import random

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

# Función para contar conflictos de una variable con un valor
def contar_conflictos(asignacion, var, valor):
    conflictos = 0
    for vecino in vecinos[var]:
        if vecino in asignacion and asignacion[vecino] == valor:
            conflictos += 1
    return conflictos

# Algoritmo de Mínimos Conflictos
def min_conflicts(max_intentos=1000):
    # Paso 1: Asignación inicial aleatoria
    asignacion = {}
    for var in variables:
        asignacion[var] = random.choice(dominios[var])

    # Paso 2: Mejorar la asignación
    for intento in range(max_intentos):
        # Encontramos variables en conflicto
        conflictos = [var for var in variables if contar_conflictos(asignacion, var, asignacion[var]) > 0]
        
        # Si no hay conflictos, terminamos
        if not conflictos:
            return asignacion

        # Elegimos una variable en conflicto aleatoriamente
        var = random.choice(conflictos)

        # Buscamos el mejor valor para minimizar conflictos
        mejor_valor = min(dominios[var], key=lambda valor: contar_conflictos(asignacion, var, valor))

        # Asignamos el mejor valor encontrado
        asignacion[var] = mejor_valor

    return None  # No se encontró solución en los intentos permitidos

# Ejecutamos el algoritmo
solucion = min_conflicts()

# Mostramos la solución
if solucion:
    print("Solución encontrada:")
    for var, valor in solucion.items():
        print(f"{var}: {valor}")
else:
    print("No se encontró solución en el número de intentos.")
