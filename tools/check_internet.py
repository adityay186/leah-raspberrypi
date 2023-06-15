import time
import socket
import os

def check_internet_connection():
    while True:
        try:
            # Attempt to create a socket and connect to www.google.com
            socket.create_connection(("www.google.com", 80))
            print("Connected to the internet.")
            os.system("mpg123 /home/leah/Documents/leah-final/tools/connected_successfully.mp3")
            break  # Break out of the loop if connection is successful
        except OSError:
            print("No internet connection. Retrying in 5 seconds...")
            os.system("mpg123 /home/leah/Documents/leah-final/tools/no_internet.mp3")
            time.sleep(5)  # Wait for 5 seconds before retrying
