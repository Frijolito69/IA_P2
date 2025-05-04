# Definimos las variables (países)
variables = ['A', 'B', 'C', 'D']

# Definimos el dominio (colores posibles)
dominios = {
    'A': ['rojo', 'verde', 'azul'],
    'B': ['rojo', 'verde', 'azul'],
    'C': ['rojo', 'verde', 'azul'],
    'D': ['rojo', 'verde', 'azul'],
}

# Definimos las restricciones de vecinos
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Función para verificar que dos vecinos no tengan el mismo color
def es_valido(asignacion, var, valor):
    for vecino in vecinos[var]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

# Algoritmo de búsqueda por retroceso (backtracking)
def backtracking(asignacion):
    # Si todas las variables están asignadas, regresamos la solución
    if len(asignacion) == len(variables):
        return asignacion
    
    # Elegimos una variable no asignada
    var = [v for v in variables if v not in asignacion][0]
    
    # Intentamos asignar un valor del dominio
    for valor in dominios[var]:
        if es_valido(asignacion, var, valor):
            # Asignamos temporalmente
            asignacion[var] = valor
            resultado = backtracking(asignacion)
            if resultado:
                return resultado
            # Si no funciona, deshacemos la asignación
            del asignacion[var]
    
    return None

# Ejecutar la búsqueda
solucion = backtracking({})

# Mostrar la solución encontrada
if solucion:
    print("Solución encontrada:")
    for var, valor in solucion.items():
        print(f"{var}: {valor}")
else:
    print("No se encontró solución.")
