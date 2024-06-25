# pip install gtts pygame
# pip install PyAudio
# pip install SpeechRecognition
import speech_recognition as sr
from gtts import gTTS
import pygame
import io

# Initialize the recognizer
recognizer = sr.Recognizer()

def sound(mytext):
    myobj = gTTS(text=mytext, lang='en', slow=False)

    # Create a byte stream to hold the audio data
    audio_fp = io.BytesIO()
    myobj.write_to_fp(audio_fp)
    audio_fp.seek(0)

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(audio_fp, 'mp3')
    pygame.mixer.music.play()

    # Keep the script running until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Use the microphone as the source for input
def voice(msg):
    sound(msg)
    with sr.Microphone() as source:
        sound("Please wait. Calibrating microphone...")
        # Listen for 5 seconds and create the ambient noise energy level
        recognizer.adjust_for_ambient_noise(source, duration=5)
        sound("Microphone calibrated. Say something!")

        # Capture the audio from the microphone
        audio = recognizer.listen(source)

    try:
        # Recognize the speech using Google's web API
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return text

msg = "Stranger detected, do you want to save their contacts?"
text = voice(msg)
if (text=="yes"):
    query = "What's their name"
    name = "Nice to meet you" + voice(query)
    sound(name)
else:
    sound("Okay then")
