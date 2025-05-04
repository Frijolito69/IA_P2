# Definimos las probabilidades del clima
probabilidades_clima = {
    'soleado': 0.7,
    'lluvioso': 0.3
}

# Definimos la utilidad de cada decisión en cada clima
utilidades = {
    ('soleado', 'ir'): 10,
    ('lluvioso', 'ir'): -20,
    ('soleado', 'no_ir'): 0,
    ('lluvioso', 'no_ir'): 0
}

# Función para calcular utilidad esperada sin preguntar
def utilidad_sin_informacion():
    ue_ir = 0
    ue_no_ir = 0
    for clima, prob in probabilidades_clima.items():
        ue_ir += prob * utilidades[(clima, 'ir')]
        ue_no_ir += prob * utilidades[(clima, 'no_ir')]
    return max(ue_ir, ue_no_ir)

# Función para calcular utilidad esperada preguntando el clima
def utilidad_con_informacion():
    # Soleado → ir
    utilidad_soleado = utilidades[('soleado', 'ir')]
    # Lluvioso → no ir
    utilidad_lluvioso = utilidades[('lluvioso', 'no_ir')]
    
    return (probabilidades_clima['soleado'] * utilidad_soleado +
            probabilidades_clima['lluvioso'] * utilidad_lluvioso)

# Cálculos
ue_sin_info = utilidad_sin_informacion()
ue_con_info = utilidad_con_informacion()

# Calculamos VOI
valor_de_la_informacion = ue_con_info - ue_sin_info

# Mostramos resultados
print(f"Utilidad esperada sin información: {ue_sin_info}")
print(f"Utilidad esperada con información: {ue_con_info}")
print(f" Valor de la información: {valor_de_la_informacion}")

if valor_de_la_informacion > 0:
    print(" Conviene preguntar el pronóstico.")
else:
    print(" No conviene preguntar el pronóstico.")
