import pyttsx3
import os
import sys
from yolov5 import detect
import time 

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('volume', 1.0)  # Set volume to max

# Check available voices
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)  # Use the first available voice
else:
    print("No voices found! TTS may not work.")

last_index = 0

def detect_sign_language(source):
    results = detect.run(weights='best.pt', source=source)
    # if results[last_index]:
    current_result = results[last_index]
    print(f"Error with pyttsx3: {e}")
    os.system(f'say "{current_result}"')  # macOS fallback
    #time.sleep(1)

if __name__ == "__main__":
    source = sys.argv[1] if len(sys.argv) > 1 else 0
    detect_sign_language(source)
    last_index += 1

