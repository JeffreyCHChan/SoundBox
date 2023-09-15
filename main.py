from playsound import playsound
import os
import RPi.GPIO as GPIO

channels = [16, 18, 22, 32]
files = os.listdir("Sounds")
sounds = {}
for count, channel in enumerate(channels.keys()):
    sounds[channel] = files[count]

# Define a callback function to be called when the button is pushed
def button_callback(channel):
    if channel == 16:
        playsound(sounds[channel])
    elif channel == 18:
        playsound(sounds[channel])
    elif channel == 22:
        playsound(sounds[channel])
    elif channel == 32:
        playsound(sounds[channel])

# Ignore GPIO setup warnings
GPIO.setwarnings(False)

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Set up input pins with pull-down resistors

for channel in channels:
    GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set up event detection for rising edges on all channels
for channel in channels:
    GPIO.add_event_detect(channel, GPIO.RISING, callback=button_callback)

message = input("Press enter to quit\n\n")  # Run until someone presses enter

# Clean up GPIO resources when done
GPIO.cleanup()
