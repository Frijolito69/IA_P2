# Definimos la distribución de un dado
distribucion = {
    1: 1/6,
    2: 1/6,
    3: 1/6,
    4: 1/6,
    5: 1/6,
    6: 1/6
}

# Mostrar la distribución
print("Distribución de Probabilidad del dado:")
for cara, probabilidad in distribucion.items():
    print(f"Cara {cara}: Probabilidad {probabilidad:.2f}")

# Verificar que las probabilidades sumen 1
suma_probabilidades = sum(distribucion.values())
print(f"Suma de todas las probabilidades: {suma_probabilidades}")
