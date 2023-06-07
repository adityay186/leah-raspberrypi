import sys
sys.path.append("/home/leah/Documents/leah-final/")
sys.path.append("/home/leah/Documents/leah-final/tts_engine")

from skills import weather
from skills import time
from skills import search
from skills import news
from skills import send_message

# Mapping of intent types to corresponding skill functions
intent_handlers = {
    'weather': weather.get_weather,
    'time' : time.get_time,
    'search_summary' : search.searchSummary,
    'news' : news.playNews,
    'send_message' : send_message.send_message
    # Add more intent types and corresponding handlers as needed
}

def process_intent(intent):
    intent_type = intent.get('intent_type')
    if intent_type in intent_handlers:
        # Call the corresponding handler function based on intent_type
        res = intent_handlers[intent_type](intent)
        return res
    else:
        # Default handler for unknown intent types
        print("Unknown intent type")
        return " "
