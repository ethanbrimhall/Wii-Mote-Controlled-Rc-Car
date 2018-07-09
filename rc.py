import cwiid #wii controller library
from time import sleep
import RPi.GPIO as gpio

print("Press 1 + 2 to pair Wiimote")
sleep(1)
paired = False
while paired == False:
        try:
                wii = cwiid.Wiimote()
                paired = True
        except:
                paired = False

wii.rpt_mode = cwiid.RPT_BTN

def init():
        gpio.setmode(gpio.BOARD)
        gpio.setup(7, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)


def forward(tf):
        init()
        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, True)
        gpio.output(15, False)
        print("Going forward")
        sleep(tf)
        gpio.cleanup()

def reverse(tf):
        init()
        gpio.output(7, True)
        gpio.output(11, False)
        gpio.output(13, False)
        gpio.output(15, True)
        print("Going backward")
        sleep(tf)
        gpio.cleanup()

def turnRight(tf):
        init()
        gpio.output(7, False)
        gpio.output(11, True)
        gpio.output(13, False)
        gpio.output(15, False)
        print("Going right")
        sleep(tf)
        gpio.cleanup()

#0.03 is how long to sleep after each button press
def key_pressed():
        while True:
                buttons = wii.state['buttons']
                if(buttons & cwiid.BTN_DOWN):
                        if(buttons & cwiid.BTN_2):
                                turnRight(0.03)
                elif(buttons & cwiid.BTN_UP):
                        if(buttons & cwiid.BTN_2):
                                turnLeft(0.03)
                elif(buttons & cwiid.BTN_2):
                        forward(0.03)
                elif(buttons & cwiid.BTN_1):
                        reverse(0.03)

key_pressed()
