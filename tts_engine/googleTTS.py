from gtts import gTTS
import pygame
import os

class GoogleTTS:
    def __init__(self, text):
        print("::creating gTTS object::")
        self.language = "en"
        self.text = text

    def play(self):
        if self.text == None or self.text == "" or self.text == " ":
                pass
        
        else:
                # Create a gTTS object
                tts = gTTS(text=self.text, lang=self.language)

                # Save the speech as an MP3 file
                print("::saving audio::")
                tts.save("tts.mp3")

                os.system("mpg123 tts.mp3")
                os.remove("tts.mp3")
