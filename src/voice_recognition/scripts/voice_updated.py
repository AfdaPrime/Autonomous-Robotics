#!/usr/bin/env python3
# pip install gtts pygame
# pip install PyAudio
# pip install SpeechRecognition
# pip install keyboard
import speech_recognition as sr
from gtts import gTTS
import pygame
import io
from voice_recognition.srv import strangerPrompt,strangerPromptResponse
import rospy

# Initialize the recognizer
recognizer = sr.Recognizer()
pygame.mixer.init()

def sound(mytext):
    myobj = gTTS(text=mytext, lang='en', slow=False)

    # Create a byte stream to hold the audio data
    audio_fp = io.BytesIO()
    myobj.write_to_fp(audio_fp)
    audio_fp.seek(0)

    # Initialize pygame mixer

    pygame.mixer.music.load(audio_fp, 'mp3')
    pygame.mixer.music.play()

    # Keep the script running until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Use the microphone as the source for input
def voice(msg):

    # Play the sound of the message
    sound("Please wait. Calibrating microphone...")

    with sr.Microphone() as source:

        # Listen for 5 seconds and create the ambient noise energy level
        recognizer.adjust_for_ambient_noise(source, duration=5)

        #waiting_sound.stop()

        sound("Microphone calibrated. Say something! " + msg)

        # Capture the audio from the microphone

        while True:
            audio = recognizer.listen(source)

            try:
                # Recognize the speech using Google's web API
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")

                return text
  

            except sr.UnknownValueError:
                sound("Sorry, I could not understand the audio. Please Repeat")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except KeyboardInterrupt:
                SystemExit()
            except Exception as e:
                print(e)

def handle_respond(req):
    # Beep sound started

    #pygame.mixer.init()
    beep = pygame.mixer.Sound("/home/vboxuser/ws_catkin/beep.mp3")  # Put the song path accordingly
    beep.play()

    # Press button "s" in keyboard first or any button

    text = voice("Do you wish to proceed to save contact?")

    if(text=="yes"):
        query = "What's their name?"
        name = voice(query)
        sound("Contact saved. Nice to meet you" + name)
    else:
        name = "stranger"
        sound("Saving contact cancelled.")

    return strangerPromptResponse(name)

def main():
    s = rospy.Service('strangerPrompt',strangerPrompt,handle_respond)
    rospy.spin()
    


if __name__ =="__main__":
    rospy.init_node("voice_recognitor")
    main()