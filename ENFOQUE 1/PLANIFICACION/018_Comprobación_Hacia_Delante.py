# Variables (países)
variables = ['A', 'B', 'C', 'D']

# Dominios (colores posibles)
dominios_originales = {
    'A': ['rojo', 'verde', 'azul'],
    'B': ['rojo', 'verde', 'azul'],
    'C': ['rojo', 'verde', 'azul'],
    'D': ['rojo', 'verde', 'azul'],
}

# Vecinos (países adyacentes)
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Función para checar si la asignación es válida
def es_valido(asignacion, var, valor):
    for vecino in vecinos[var]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

# Función de Forward Checking
def forward_check(dominios, var, valor):
    dominios_reducidos = {}

    # Recorremos los vecinos del nodo asignado
    for vecino in vecinos[var]:
        if vecino not in dominios:
            continue  # Saltamos vecinos ya asignados

        # Guardamos el dominio anterior por si necesitamos retroceder
        dominio_anterior = dominios[vecino][:]
        
        # Eliminamos valores que ya no son posibles
        dominios[vecino] = [v for v in dominios[vecino] if v != valor]
        
        dominios_reducidos[vecino] = dominio_anterior  # Guardamos copia por si fallamos
        
        # Si algún dominio se vacía, fallamos
        if not dominios[vecino]:
            return None, dominios_reducidos

    return dominios, dominios_reducidos

# Algoritmo de Backtracking con Forward Checking
def backtracking_fc(asignacion, dominios):
    # Si todas las variables están asignadas, retornamos la solución
    if len(asignacion) == len(variables):
        return asignacion

    # Elegimos una variable no asignada
    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        if es_valido(asignacion, var, valor):
            asignacion[var] = valor

            # Hacemos Forward Checking
            dominios_copia = {v: dominios[v][:] for v in dominios}
            dominios_actualizados, cambios = forward_check(dominios_copia, var, valor)

            if dominios_actualizados is not None:
                resultado = backtracking_fc(asignacion, dominios_actualizados)
                if resultado:
                    return resultado

            # Retrocedemos
            del asignacion[var]

    return None

# Copiamos los dominios iniciales para empezar
dominios = {v: dominios_originales[v][:] for v in variables}

# Ejecutamos el backtracking con forward checking
solucion = backtracking_fc({}, dominios)

# Mostramos la solución encontrada
if solucion:
    print("Solución encontrada:")
    for var, valor in solucion.items():
        print(f"{var}: {valor}")
else:
    print("No se encontró solución.")
