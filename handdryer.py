'''
Property of Austen II
Raspberry Pi Motion-Activated Fan
feel free to use and modify whatever
we're all here to learn and grow n stuff
'''
# Import libraries
import RPi.GPIO as GPIO
import time

# Python functions
# GPIO Basic Initialization
def init(numtype, pirpin, fanpin):
    checker(numtype, pirpin, fanpin)
    # The only options are BOARD and BCM and the checker would've caught errors
    if numtype.upper() == "BOARD":
        GPIO.setmode(GPIO.BOARD)
    else:
        GPIO.setmode(GPIO.BCM)
    # Sets up the respective pins
    GPIO.setup(pirpin, GPIO.IN)
    GPIO.setup(fanpin, GPIO.OUT, initial=GPIO.LOW) # Just in case :)

# Ensures proper inputs were given to not break stuff (my circuitry is jank)
def checker(numtype, pirpin, fanpin):
    if numtype.upper() == "BOARD":
        GPIO.setmode(GPIO.BOARD)
        invalid_board_numbers = [1, 2, 4, 6, 9, 14, 17, 20, 25, 30, 34, 39]
        problem = 0
        if pirpin in invalid_board_numbers:
            print("PIR sensor is connected to an invalid pin, slow down ;)")
            problem = 1
        if fanpin in invalid_board_numbers:
            print("Fan is connected to an invalid pin, 'cool' your jets :p")
            problem = 1
        if problem == 1:
            exit(1)
    elif numtype.upper() == "BCM":
        GPIO.setmode(GPIO.BCM)
        # Due to what BCM is, it doesn't need to check for invalid numbers
    else:
        print("Invalid board numbering type.")
        exit(1)

def dryer(pirpin, fanpin):
    # The max timer decides the max amount of loops this will run before
    #  this program cleans up. This is because I have a dodgy circuit
    #  and I want to make sure I run the cleanup before it catches fire.
    # The standby variable declares the amount of loops without motion
    #  before the fan turns off and goes back to "standby mode"
    max_timer = 200
    standby = 5
    pause = 0
    
    while max_timer > 0:
        # No while loops to create a predictable execution time
        if GPIO.input(pirpin) > 0:
            GPIO.output(fanpin, 1)
            pause = standby
        elif pause > 0:
            pause -= 1
            if pause == 0: print("standby triggered")
        else:
            GPIO.output(fanpin, 0)
        max_timer -= 1
        if (max_timer % 10) == 0:
            print("max: ", max_timer)
        time.sleep(0.1)
    
    
# Start of program
# Change these variables yourself, I intentionally don't create
#  a whole "hey there, which numbering type / pin would you like to use?" because
#  when I press run I want it to just start rather than ask the same question every
#  time when the circuit is the same circuit that was set up the last 10 times I ran the code.
num = "board"
pir = 7
fan = 8
init(num, pir, fan)
# Could set GPIO.setwarnings(False) but I leave it out so I can break code and learn

print("Waiting for pir signal")
while GPIO.input(pir) < 1:
    time.sleep(0.2)

# And we're on...
dryer(pir, fan)

# Cleanup resources to avoid XK-Class scenarios
#  Note: will only clean up pins that script used.
GPIO.cleanup()