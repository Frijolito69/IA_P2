# Estados ocultos
estados = ['Soleado', 'Lluvioso']

# Observaciones
observaciones = ['P', 'P', 'N']

# Matriz de transición
transicion = {
    'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

# Matriz de emisión
emision = {
    'Soleado': {'P': 0.1, 'N': 0.9},
    'Lluvioso': {'P': 0.8, 'N': 0.2}
}

# Probabilidades iniciales
inicio = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Algoritmo de Viterbi
def viterbi(obs, estados, inicio, transicion, emision):
    V = [{}]  # Tabla de Viterbi

    # Inicializar primera observación
    for estado in estados:
        V[0][estado] = {
            'prob': inicio[estado] * emision[estado][obs[0]],
            'prev': None
        }

    # Resto de observaciones
    for t in range(1, len(obs)):
        V.append({})
        for estado in estados:
            max_tr_prob = max(V[t-1][prev_estado]['prob'] * transicion[prev_estado][estado] for prev_estado in estados)
            for prev_estado in estados:
                if V[t-1][prev_estado]['prob'] * transicion[prev_estado][estado] == max_tr_prob:
                    max_prob = max_tr_prob * emision[estado][obs[t]]
                    V[t][estado] = {'prob': max_prob, 'prev': prev_estado}
                    break

    # Reconstruir la mejor ruta
    opt = []
    # Escoger el último estado con mayor probabilidad
    max_prob = max(value['prob'] for value in V[-1].values())
    previous = None
    for estado, data in V[-1].items():
        if data['prob'] == max_prob:
            opt.append(estado)
            previous = estado
            break

    # Retroceder para encontrar el camino completo
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]['prev'])
        previous = V[t + 1][previous]['prev']

    print(f"La secuencia más probable de estados es: {opt}")
    print(f"La probabilidad de esta secuencia es: {max_prob:.5f}")

# Ejecutar
viterbi(observaciones, estados, inicio, transicion, emision)
