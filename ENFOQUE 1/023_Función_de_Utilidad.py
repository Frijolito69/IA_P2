# Definimos utilidades de cada resultado
utilidades = {
    'ganar': 100,
    'perder': -40,
    'no_apostar': 0
}

# Definimos probabilidades de cada resultado
probabilidades = {
    'ganar': 0.5,
    'perder': 0.5,
    'no_apostar': 1.0  # Si no apuestas, certeza de no cambiar
}

# Función para calcular utilidad esperada
def utilidad_esperada(accion):
    if accion == 'apostar':
        return (probabilidades['ganar'] * utilidades['ganar'] +
                probabilidades['perder'] * utilidades['perder'])
    elif accion == 'no_apostar':
        return utilidades['no_apostar']
    else:
        return None

# Calculamos utilidades esperadas
ue_apostar = utilidad_esperada('apostar')
ue_no_apostar = utilidad_esperada('no_apostar')

print(f"Utilidad esperada al apostar: {ue_apostar}")
print(f"Utilidad esperada al no apostar: {ue_no_apostar}")

# Elegimos la mejor acción
if ue_apostar > ue_no_apostar:
    print(" Mejor decisión: Apostar")
else:
    print(" Mejor decisión: No apostar")
