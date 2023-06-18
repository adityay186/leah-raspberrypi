from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

engine = IntentDeterminationEngine()

# intent definition begins

# WEATHER INTENT
##############################################################
weather_keyword = [
    "weather",
    "forecast",
    "temperature"
]

for wk in weather_keyword:
    engine.register_entity(wk, "weatherKeyword")

engine.register_regex_entity("(?:in|of|at) (?P<location>.*)")

weather_intent = IntentBuilder("weather")\
    .require("weatherKeyword")\
    .require("location")\
    .build()

engine.register_intent_parser(weather_intent)
##############################################################

# TIME INTENT
##############################################################
time_keyword = [
    "time"
]

for tk in time_keyword:
    engine.register_entity(tk, "timeKeyword")

time_intent = IntentBuilder("time") \
    .require("timeKeyword") \
    .build()

engine.register_intent_parser(time_intent)
##############################################################

# SEARCH_SUMMARY INTENT
##############################################################
search_keyword = [
    "search",
    "understand",
    "mean"
]

for sk in search_keyword:
    engine.register_entity(sk, "searchKeyword")

engine.register_regex_entity(".*(?:by|is|a|is a|for) (?P<search_entity>.*)")

search_summary_intent = IntentBuilder("search_summary") \
    .require("searchKeyword")\
    .require("search_entity") \
    .build()

engine.register_intent_parser(search_summary_intent)
##############################################################

# NEWS INTENT
##############################################################
news_keywords = [
    "news",
    "headlines"
]
for nk in news_keywords:
    engine.register_entity(nk, "newsKeywords")

news_cat = [
    'hindi',
    'english'
]

for nc in news_cat:
    engine.register_entity(nc, "newsCategory")

# Define NewsIntent
news_intent = IntentBuilder("news") \
    .require("newsKeywords") \
    .optionally("newsCategory")\
    .build()

# Register the NewsIntent
engine.register_intent_parser(news_intent)
##############################################################

# SEND MESSAGE INTENT
##############################################################
send_message_keywords = [
    "send",
    "message"
]

for smk in send_message_keywords:
    engine.register_entity(smk, "sendMessageKeywords")

message_category = [
    "telegram",
    "email",
    "mail"
]

for mc in message_category:
    engine.register_entity(mc, "sendMessageCategory")

sent_message_intent = IntentBuilder("send_message")\
    .require("sendMessageKeywords")\
    .optionally("sendMessageCategory")\
    .build()

engine.register_intent_parser(sent_message_intent)
##############################################################

# SONG RECOGNITION INTENT
song_recognition_keywords = [
    "song",
    "music"
]

for srk in song_recognition_keywords:
    engine.register_entity(srk, "songRecognitionKeywords")

song_recognition_keywords2 = [
    "what",
    "which",
    "identify"
]

for srk2 in song_recognition_keywords2:
    engine.register_entity(srk2, "songRecognitionKeywords2")

song_recognition_intent = IntentBuilder("song_recognise")\
    .require("songRecognitionKeywords")\
    .require("songRecognitionKeywords2")\
    .build()

engine.register_intent_parser(song_recognition_intent)
##############################################################

# DAILY QUOTES STOP/START INTENT
daily_quotes_keywords = [
    "quotes",
    "quote",
    "motivation",
    "daily motivation"
]

for dqk in daily_quotes_keywords:
    engine.register_entity(dqk, "dailyQuotesKeywords")

daily_quotes_action = [
    "stop",
    "start"
]

for dqa in daily_quotes_action:
    engine.register_entity(dqa, "dailyQuotesAction")

daily_quotes_intent = IntentBuilder("daily_quotes")\
    .require("dailyQuotesKeywords")\
    .require("dailyQuotesAction")\
    .build()

engine.register_intent_parser(daily_quotes_intent)
##############################################################

# DOCTOR INTENT
sick_keywords = [
    "doctor",
    "sick",
    "unwell",
    "not well",
    "not feeling good",
    "not feeling well"
]

for sick_keyword in sick_keywords:
    engine.register_entity(sick_keyword, "sickKeywords")

doctor_intent = IntentBuilder("be_a_doctor")\
    .require("sickKeywords")\
    .build()

engine.register_intent_parser(doctor_intent)
##############################################################

# HOME SECURITY INTENT
home_security_keywords = [
    "monitoring",
    "monitor"
]

for hsk in home_security_keywords:
    engine.register_entity(hsk, "homeSecurityKeywords")

home_security_action = [
    "start",
    "stop"
]

for hsa in home_security_action:
    engine.register_entity(hsa, "action")

home_security_intent = IntentBuilder("home_security")\
    .require("homeSecurityKeywords")\
    .require("action")\
    .build()

engine.register_intent_parser(home_security_intent)
##############################################################
    
# intent definition ends

def get_intent(command, sr_obj, tts_obj):
    intents = list(engine.determine_intent(command))
    if intents:
        for intent in intents:
            if intent.get('confidence') > 0:
                intent['sr_obj'] = sr_obj
                intent['tts_obj'] = tts_obj
                return intent
    else:
        return {"intent_type" : "null"}