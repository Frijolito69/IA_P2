# Ejemplo de probabilidad condicionada

# Probabilidades conocidas
P_B = 0.5          # Probabilidad de que ocurra B
P_A_y_B = 0.2      # Probabilidad de que ocurra A y B al mismo tiempo

# Cálculo de la probabilidad condicionada
P_A_dado_B = P_A_y_B / P_B

print(f"Probabilidad de A dado B: {P_A_dado_B:.2f}")

# Ahora un ejemplo de normalización
valores = {
    "A": 2,
    "B": 5,
    "C": 3
}

# Suma de los valores
suma_total = sum(valores.values())

# Normalizamos
valores_normalizados = {k: v / suma_total for k, v in valores.items()}

print("Valores normalizados:")
for k, v in valores_normalizados.items():
    print(f"{k}: {v:.2f}")
