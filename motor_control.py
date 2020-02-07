import RPi.GPIO as GPIO
import time
import keyboard
import sys, tty, termios

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Pins being used to control motors
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(16, GPIO.IN)

    while True:
        char = getch()
        # move forward if w is pressed
        if (char == "w"):
            forward()
            
        # turn left if a is pressed
        if (char == "a"):
            left()
            
        # turn right if d is pressed
        if (char == "d"):
            right()
            
        # move backwards if s is pressed
        if (char == "s"):
            reverse()
            
        # Brake statement - temporarily used to stop motors
        if (char == "b"):
            stop()
            
        # EXIT LOOP
        if (char == "p"):
            break
            
            
###### PROXIMITY CENSOR CODE 4-10############
##    while True:
##        if (GPIO.input(16) == True):
##            forward()
##        if (GPIO.input(16) == False):
##            stop()
##            time.sleep(1)
##            reverse()
##            time.sleep(1)
##            stop()
##            time.sleep(1)
##            right()
##            time.sleep(1)
##            stop()
##            time.sleep(1)
            
# CODE FROM: https://www.instructables.com/id/Controlling-a-Raspberry-Pi-RC-Car-With-a-Keyboard/
# returns key pressed
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# method to make the motors guide the vehicle forward
def forward():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
# method to make the motors guide the vehicle backwards
def reverse():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
# method to make the motors guide the vehicle to turn left
def left():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
# method to make the motors guide the vehicle to turn right
def right():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
# method that stops all motors of the vehicle
def stop():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)

main()
