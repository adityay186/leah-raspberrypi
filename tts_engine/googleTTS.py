from gtts import gTTS
import os
import sys

sys.path.append("/home/leah/Documents/leah-final/tools")

from mpg123_player import play_mpg123

class GoogleTTS:
    def __init__(self, text):
        #print("::creating gTTS object::")
        self.language = "en"
        self.text = text

    def play(self):
        if self.text == None or self.text == "" or self.text == " ":
            pass
        else:
            try:
                # Create a gTTS object
                tts = gTTS(text=self.text, lang=self.language)

                # Save the speech as an MP3 file
                #print("::saving audio::")
                tts.save("tts.mp3")

                # Play the audio using os.system
                print("::Playing TTS:: \n")
                play_mpg123("tts.mp3")
                print("::Done Playing:: \n")

            except Exception as e:
                print("An error occurred:", str(e))
                play_mpg123("something_went_wrong.mp3")

            finally:
                # Remove the temporary audio file
                if os.path.exists("tts.mp3"):
                    os.remove("tts.mp3")

