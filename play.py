from playsound import playsound
import pyttsx3 as pt
def play(audio):
    playsound(audio)
def speak(text):
    engine=pt.init()
    engine.say(text)
    engine.runAndWait()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("your voice is being captured")
        audio = r.listen(source)
        try:
            a = r.recognize_google(audio)
            print("you said:{}", format(a))
        except:
            speak("unable to recognize your voice due to background disturbances ")

