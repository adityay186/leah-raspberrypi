import os

sys.path.append("/home/leah/Documents/leah-final/tools")

from mpg123_player import play_mpg123

play_mpg123("/home/leah/Documents/leah-final/wake_word_engine/leah_startup_sound.mp3")

play_mpg123("/home/leah/Documents/leah-final/wake_word_engine/please_wait.mp3")

print("IMPORTING REQUIRED LIBRARIES..")
import struct
import pyaudio
import pvporcupine
import sys

print("IMPORTING MORE LIBRARIES..")
sys.path.append("/home/leah/Documents/leah-final/tts_engine")
sys.path.append("/home/leah/Documents/leah-final/intent_engine")
sys.path.append("/home/leah/Documents/leah-final/skill_handle")

print("IMPORTING FUNCTIONS..")
from intent import get_intent
from skill_handler import process_intent
from googleTTS import GoogleTTS
import speech_recognition as sr
from playsound import playsound
from color_print import print_green
from check_internet import check_internet_connection

def detect_wake_word():
    print("INITIALIZING WAKE WORD ENGINE..")
    porcupine = None
    pa = None
    audio_stream = None

    keys = {
            "adityay186@gmail.com" : "61LuNHOI0Wkh4yBbrkck+HDV39muOqtQF3oevQE3Xt+DhIuiWzo1zg==",
            "20190802060@dypiu.ac.in" : "Zb5nW42pBDH0wOptYTK1neJ1fyrYWPJZv0T0IfkFQKmzXTlQZuo24w=="
    }

    tts = GoogleTTS("")
    r = sr.Recognizer()

    try:
        porcupine = pvporcupine.create(access_key = keys["adityay186@gmail.com"],
                                        keyword_paths = ["hey_leah-raspberry_pi/hey_leah-raspberry_pi.ppn"])

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
                        rate=porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=porcupine.frame_length)
        
        check_internet_connection()

        print("WAKE WORD ENGINE RUNNING..")

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                print_green("WAKE WORD DETECTED!")
                command = None
                with sr.Microphone() as source:
                    print("Speak ...... ")
                    play_mpg123("start_sound.mp3")
                    audio = r.listen(source, phrase_time_limit = 4)
                try:
                    command = r.recognize_google(audio)
                    print(command)
                except sr.UnknownValueError:
                    er = "sorry, could not recognize"
                    tts.text = er
                    print(er)
                    tts.play()
                    continue
                except sr.RequestError as e:
                    er2 = "Could not request results"
                    tts.text = er2
                    print(er2)
                    tts.play()
                    continue

                intention = get_intent(command, r, tts)
                print(intention)
                res = process_intent(intention)
                tts.text = res
                print(res)
                tts.play()

                
    finally:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
                pa.terminate()

detect_wake_word()
