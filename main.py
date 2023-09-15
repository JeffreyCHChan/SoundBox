import os
import RPi.GPIO as GPIO

channels = [8,10,16,18]
files = os.listdir("Sounds")
sounds = {}
print(files)
for count, channel in enumerate(channels):
    sounds[channel] = "Sounds/"+files[count]
    
print(sounds)

# Define a callback function to be called when the button is pushed
def button_callback(channel):    
#     print("Channel "+ channel)
    file = sounds[channel]
    os.system("mpg123 "+file)


# Ignore GPIO setup warnings
GPIO.setwarnings(False)

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

for channel in channels:
    GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set up event detection for rising edges on all channels
for channel in channels:
    GPIO.add_event_detect(channel, GPIO.RISING, callback=button_callback)

message = input("Press enter to quit\n\n")  # Run until someone presses enter

# Clean up GPIO resources when done
GPIO.cleanup()

