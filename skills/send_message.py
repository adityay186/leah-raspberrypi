import asyncio
import telegram
import speech_recognition as sr

tts_obj = None
sr_obj = None

def get_stt():
    tts_obj.text = "what is the message?"
    tts_obj.play()

    stt = None

    with sr.Microphone() as source:
        print("speak the message .. ")
        audio = sr_obj.listen(source, phrase_time_limit = 5)
    try:
        stt = sr_obj.recognize_google(audio)
        print(stt)
        return stt
    except sr.UnknownValueError:
        er = "sorry could not recognize"
        tts_obj.text = er
        print(er)
        tts_obj.play()
        return er
    except sr.RequestError as e:
        er2 = "could not fech results"
        tts_obj.text = er2
        print(er2)
        tts_obj.play()
        return er2

async def send_telegram_message(message):
    # Set your bot token and chat ID
    bot_token = '6192792234:AAEiAxGK_qweROD-88YgnGWoWyAoahTE9P8'
    chat_id = '-960255198'

    # Create a bot instance
    bot = telegram.Bot(token=bot_token)

    # Send the message
    await bot.send_message(chat_id=chat_id, text=message, timeout=10)

    print("Telegram Message Delivered Successfully..")

def send_message(entities):
    global tts_obj
    tts_obj = entities['tts_obj']
    global sr_obj
    sr_obj = entities['sr_obj']

    if 'sendMessageCategory' in entities:
        if entities['sendMessageCategory'] == 'telegram':
            message = get_stt()
            loop = asyncio.get_event_loop()
            loop.run_until_complete(send_telegram_message(message))
            return "message sent successfully"
