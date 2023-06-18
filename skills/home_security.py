import os
import sys
import time

sys.path.append("/home/leah/Documents/leah-final/tools")

from tools import mpg123_player

while True:
    mpg123_player.play_mpg123("/home/leah/Documents/leah-final/tools/connected_successfully.mp3")
    time.sleep(3)
