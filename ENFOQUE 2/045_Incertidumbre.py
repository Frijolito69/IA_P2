# Definimos las probabilidades que el robot percibe
probabilidades = {
    "pelota": 0.7,  # 70% seguro que es una pelota
    "caja": 0.3     # 30% seguro que es una caja
}

# Función para decidir qué cree que es
def decidir_objeto(probabilidades):
    if probabilidades["pelota"] > probabilidades["caja"]:
        return "Creo que es una pelota."
    else:
        return "Creo que es una caja."

# Ejecutamos la función
decision = decidir_objeto(probabilidades)

print("Probabilidades percibidas:", probabilidades)
print(decision)
