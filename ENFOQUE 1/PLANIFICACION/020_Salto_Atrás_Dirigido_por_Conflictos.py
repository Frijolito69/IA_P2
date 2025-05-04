# Variables
variables = ['A', 'B', 'C', 'D']

# Dominios
dominios = {
    'A': ['rojo', 'verde'],
    'B': ['rojo', 'verde'],
    'C': ['rojo', 'verde'],
    'D': ['rojo', 'verde'],
}

# Vecinos
vecinos = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['A']
}

# Función que chequea validez
def es_valido(asignacion, var, valor):
    for vecino in vecinos[var]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

# Algoritmo de Salto Atrás Dirigido por Conflictos
def backjump(asignacion, conflictos):
    # Si todas las variables están asignadas, retornamos éxito
    if len(asignacion) == len(variables):
        return asignacion, None

    # Elegimos la próxima variable a asignar
    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        if es_valido(asignacion, var, valor):
            asignacion[var] = valor

            # Inicializamos conflictos para esta variable
            conflictos[var] = set()

            resultado, conflicto = backjump(asignacion, conflictos)
            if resultado is not None:
                return resultado, None

            if conflicto is not None and var not in conflicto:
                # Propagamos conflicto hacia atrás
                return None, conflicto

        # Si no es válido, registramos conflictos
        for vecino in vecinos[var]:
            if vecino in asignacion:
                conflictos[var].add(vecino)

    # No pudimos asignar, informamos conflicto
    conflictos_del_var = conflictos.get(var, set())
    return None, conflictos_del_var

# Ejecutamos
asignacion_inicial = {}
conflictos_inicial = {}

solucion, conflicto = backjump(asignacion_inicial, conflictos_inicial)

# Mostrar resultados
if solucion:
    print("Solución encontrada:")
    for var, valor in solucion.items():
        print(f"{var}: {valor}")
else:
    print("No se encontró solución.")
