import speech_recognition as sr

# Inicializamos el reconocedor
recognizer = sr.Recognizer()

# Usamos el micrófono para capturar audio
with sr.Microphone() as source:
    print("Ajustando para ruido ambiental...")
    recognizer.adjust_for_ambient_noise(source)  # Ajusta el micrófono para ruido ambiental
    print("Di algo...")
    audio = recognizer.listen(source)  # Captura la entrada de audio

# Intentamos reconocer el audio capturado
try:
    print("Reconociendo...")
    text = recognizer.recognize_google(audio)  # Usamos el servicio de Google para reconocer el audio
    print(f"Lo que dijiste: {text}")
except sr.UnknownValueError:
    print("No pude entender lo que dijiste")
except sr.RequestError:
    print("Error al conectarse al servicio de Google")

