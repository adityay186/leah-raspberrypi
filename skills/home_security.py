import os
import sys
import time

sys.path.append("/home/leah/Documents/leah-final/tools")

from mpg123_player import play_mpg123

while True:
    play_mpg123("/home/leah/Documents/leah-final/tools/connected_successfully.mp3")
    time.sleep(3)
