import speech_recognition as sr
 
recognizer = sr.Recognizer()
 
with sr.Microphone() as microphone:
    print("Say a short sentence...")
    recognizer.adjust_for_ambient_noise(microphone, duration=5)
    audio = recognizer.listen(microphone)
 
try:
    words = recognizer.recognize_google(audio)
    print("Transcript:", words)
except sr.UnknownValueError:
    print("I couldn't understand that. Try speaking clearly.")
except sr.RequestError:
    print("The speech service could not be reached. Check the internet.")