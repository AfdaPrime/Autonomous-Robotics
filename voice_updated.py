# pip install gtts pygame
# pip install PyAudio
# pip install SpeechRecognition
# pip install keyboard
import speech_recognition as sr
from gtts import gTTS
import pygame
import io
import keyboard

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
    recognizer = sr.Recognizer()
    # Play the sound of the message
    sound(msg)

    with sr.Microphone() as source:
        sound("Please wait. Calibrating microphone...")
        
        pygame.mixer.init()
        waiting_sound = pygame.mixer.Sound("C:/Users/Idzhans Khairi/Documents/VSCode/Autonomous-Robotics/waiting.mpeg")  # Put the song path accordingly
        waiting_sound.play()

        # Listen for 5 seconds and create the ambient noise energy level
        recognizer.adjust_for_ambient_noise(source, duration=5)

        waiting_sound.stop()

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

# Beep sound started
while True:
    pygame.mixer.init()
    beep = pygame.mixer.Sound("C:/Users/Idzhans Khairi/Documents/VSCode/Autonomous-Robotics/beep.mp3")  # Put the song path accordingly
    beep.play()

    # Press button "s" in keyboard first or any button
    keyboard.wait('s')
    text = voice("Voice detecter activated. Proceed to save contact?")

    if(text=="yes"):
        query = "What's their name?"
        name = "Contact saved. Nice to meet you" + voice(query)
        sound(name)
    else:
        sound("Saving contact cancelled.")


