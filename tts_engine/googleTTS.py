from gtts import gTTS
import os

class GoogleTTS:
    def __init__(self, text):
        print("::creating gTTS object::")
        self.language = "en"
        self.text = text

    def play(self):
        try:
            # Create a gTTS object
            tts = gTTS(text=self.text, lang=self.language)

            # Save the speech as an MP3 file
            print("::saving audio::")
            tts.save("tts.mp3")

            # Play the audio using os.system
            print("::playing audio::")
            os.system("mpg123 tts.mp3")

        except Exception as e:
            print("An error occurred:", str(e))
            os.system("mpg123 something_went_wrong.mp3")

        finally:
            # Remove the temporary audio file
            if os.path.exists("tts.mp3"):
                os.remove("tts.mp3")

