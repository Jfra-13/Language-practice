import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def recognize_speech():
    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        return text.lower()
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print(f"Error en la solicitud de reconocimiento de voz: {e}")

search_keyword = recognize_speech()
if search_keyword and 'amazon' in search_keyword:
    engine.say('¿Qué quieres comprar en Amazon?')
    engine.runAndWait()
    
    product_name = recognize_speech()
    if product_name:
        url = f'https://www.amazon.es/s?k={product_name}'
        webbrowser.open(url)
