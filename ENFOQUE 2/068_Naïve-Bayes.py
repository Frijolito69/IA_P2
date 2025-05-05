# Definimos los datos
total_spam = 50
total_no_spam = 50
total_emails = 100

# Probabilidades de las clases
P_spam = total_spam / total_emails
P_no_spam = total_no_spam / total_emails

# Probabilidades condicionales
P_dinero_given_spam = 30 / 50
P_enlace_given_spam = 25 / 50
P_dinero_given_no_spam = 10 / 50
P_enlace_given_no_spam = 15 / 50

# Características observadas: el correo tiene 'dinero' y 'enlace'
# Calculamos probabilidad para Spam
P_spam_given_features = P_dinero_given_spam * P_enlace_given_spam * P_spam

# Calculamos probabilidad para No Spam
P_no_spam_given_features = P_dinero_given_no_spam * P_enlace_given_no_spam * P_no_spam

# Mostramos resultados
print(f"Probabilidad de Spam: {P_spam_given_features:.4f}")
print(f"Probabilidad de No Spam: {P_no_spam_given_features:.4f}")

# Decisión final
if P_spam_given_features > P_no_spam_given_features:
    print("El correo es clasificado como: SPAM")
else:
    print("El correo es clasificado como: NO SPAM")
