import random

# Definimos eventos y sus probabilidades
eventos = ['gripe', 'alergia']
probabilidades = [0.9, 0.1]  # 90% gripe, 10% alergia

# Elegimos un diagnóstico según las probabilidades
diagnostico = random.choices(eventos, weights=probabilidades, k=1)[0]

print(f"El diagnóstico probable es: {diagnostico}")
