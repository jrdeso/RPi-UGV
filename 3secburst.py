import RPi.GPIO as GPIO
import time
import keyboard
import sys, tty, termios

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Pin being used to control gun firing
    GPIO.setup(18, GPIO.OUT)

    print("3 Second Burst")
    
    GPIO.output(18, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(18, GPIO.LOW)

    print("End")

         
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

main()
