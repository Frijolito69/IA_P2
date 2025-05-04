import random

# Definimos las probabilidades del clima
probabilidades_clima = {
    'soleado': 0.7,
    'lluvioso': 0.3
}

# Definimos la utilidad de cada combinación
utilidad = {
    ('soleado', 'llevar_paraguas'): -2,
    ('soleado', 'no_llevar_paraguas'): 10,
    ('lluvioso', 'llevar_paraguas'): 10,
    ('lluvioso', 'no_llevar_paraguas'): -20
}

# Función para calcular utilidad esperada para una decisión
def utilidad_esperada(decision):
    ue = 0
    for clima, prob in probabilidades_clima.items():
        ue += prob * utilidad[(clima, decision)]
    return ue

# Calculamos utilidad esperada de cada decisión
ue_llevar = utilidad_esperada('llevar_paraguas')
ue_no_llevar = utilidad_esperada('no_llevar_paraguas')

# Mostramos resultados
print(f"Utilidad esperada de llevar paraguas: {ue_llevar}")
print(f"Utilidad esperada de no llevar paraguas: {ue_no_llevar}")

# Elegimos la mejor decisión
if ue_llevar > ue_no_llevar:
    print(" Mejor decisión: Llevar paraguas")
else:
    print(" Mejor decisión: No llevar paraguas")
