import itertools

# Variables
variables = ['A', 'B', 'C', 'D', 'E']

# Dominios (3 colores para evitar el problema)
dominios = {
    'A': ['rojo', 'verde', 'azul'],
    'B': ['rojo', 'verde', 'azul'],
    'C': ['rojo', 'verde', 'azul'],
    'D': ['rojo', 'verde', 'azul'],
    'E': ['rojo', 'verde', 'azul'],
}

# Vecinos (restricciones)
vecinos = {
    'A': ['B', 'E'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'A']
}

# Función que chequea validez
def es_valido(asignacion, var, valor):
    for vecino in vecinos[var]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

# Resolver el CSP restante
def resolver_restante(asignacion):
    if len(asignacion) == len(variables):
        return asignacion

    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        if es_valido(asignacion, var, valor):
            asignacion[var] = valor
            resultado = resolver_restante(asignacion)
            if resultado:
                return resultado
            del asignacion[var]

    return None

# Cutset Conditioning principal
def cutset_conditioning(corte):
    valores_corte = [dominios[var] for var in corte]
    for combinacion in itertools.product(*valores_corte):
        asignacion = dict(zip(corte, combinacion))

        valido = True
        for var in corte:
            if not es_valido(asignacion, var, asignacion[var]):
                valido = False
                break

        if not valido:
            continue

        solucion = resolver_restante(asignacion.copy())
        if solucion:
            return solucion

    return None

# Ejecutamos
corte = ['A', 'C']  # Elegimos un corte
solucion = cutset_conditioning(corte)

# Mostrar resultados
if solucion:
    print("✅ Solución encontrada:")
    for var, valor in solucion.items():
        print(f"{var}: {valor}")
else:
    print("❌ No se encontró solución.")
