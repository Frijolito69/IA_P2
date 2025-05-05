# Corpus de ejemplo (colección de frases)
corpus = [
    "voy al cine",
    "voy al mercado",
    "voy al doctor",
    "voy al cine",
    "voy al mercado",
    "voy al cine"
]

# Construimos un diccionario de bigramas
bigramas = {}

for frase in corpus:
    palabras = frase.split()
    for i in range(len(palabras) - 1):
        par = (palabras[i], palabras[i+1])
        if par in bigramas:
            bigramas[par] += 1
        else:
            bigramas[par] = 1

# Mostrar los bigramas y sus frecuencias
print("Bigramas y frecuencias:")
for par, frecuencia in bigramas.items():
    print(f"{par}: {frecuencia}")

# Función para predecir la siguiente palabra
def predecir_siguiente(palabra_actual):
    candidatos = {}
    total = 0

    for (pal1, pal2), frecuencia in bigramas.items():
        if pal1 == palabra_actual:
            candidatos[pal2] = frecuencia
            total += frecuencia

    if not candidatos:
        return "No se encontró predicción."

    # Encontrar la palabra con mayor probabilidad
    mejor_palabra = max(candidatos, key=candidatos.get)
    probabilidad = candidatos[mejor_palabra] / total

    return f"Palabra más probable: '{mejor_palabra}' con probabilidad {probabilidad:.2f}"

# Probar la predicción
print("\nPredicción siguiente palabra después de 'al':")
print(predecir_siguiente("al"))
