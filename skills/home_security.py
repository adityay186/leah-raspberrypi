import requests
import json
import time
import sys

sys.path.append("/home/leah/Documents/leah-final/tools")

from mpg123_player import play_mpg123

val = None
i = 1

def motion():
    global val
    global i
    
    link = "https://api.thingspeak.com/channels/2193643/feeds.json?api_key=22VZF8OP8OGRB66G&results=2"
    
    print("Home Monitor:")

    play_mpg123("/home/leah/Documents/leah-final/tools/please_wait_home_security.mp3")
    
    while True:
        print("Waiting 5 Seconds..")
        time.sleep(5)
        print("Sending Request..")
        r = requests.get(link)
        data = json.loads(r.text)
        
        if 'last_entry_id' in data['channel']:
            val2 = data['channel']['last_entry_id']
            
            if val is None:
                val = val2
                continue
            
            if val2 == val:
                print(i, "No Detection:", val2)
            else:
                print(i, "Motion Detected:", val2)
                val = val2
                i += 1
                play_mpg123("/home/leah/Documents/leah-final/tools/motion_detected.mp3")
                play_mpg123("/home/leah/Documents/leah-final/tools/burglar_alarm.mp3")
                play_mpg123("/home/leah/Documents/leah-final/tools/take_action_immedietly.mp3")
                print("Take Action Immediately")
                break

        else:
            print("Error: Could not retrieve data from the API")
            break

motion()

