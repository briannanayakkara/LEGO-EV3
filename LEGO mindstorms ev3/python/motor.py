from ev3dev.ev3 import *
from ev3dev2.motor import *
from time import *
from ev3dev2.display import *
from PIL import *
from img import *
from os import *
from sound import *
sound = Sound()
sound.play('/home/robot/sound/PewPew.wav').wait()

# Connect two large motors on output ports B and C
lmotor = LargeMotor('outC')
rmotor = LargeMotor('outB')

# Connect remote control
rc = RemoteControl()

# Turn leds off
Leds.all_off()

# Connect EV3 color sensor
cl = ColorSensor()

# Put the color sensor into COL-REFLECT mode
# to measure reflected light intensity.
# In this mode the sensor will return a value between 0 and 100
cl.mode = 'COL-REFLECT'

while True:
    lcd = Screen()
    logo = Image.open('/home/robot/img/brtattoo.bmp')
    lcd.image.paste(logo, (0, 0))
    lcd.update()
    sleep(1)
    # not red color
    while cl.value() < 40:
        lmotor.run_forever(speed_sp=100)
        rmotor.run_forever(speed_sp=100)
        print(cl.value())
        sleep(0.1)
    # red color
    while cl.value() > 40:
        lmotor.run_forever(speed_sp=-200)
        rmotor.run_forever(speed_sp=-200)
        sleep(1)
        lmotor.run_forever(speed_sp=70)
        rmotor.run_forever(speed_sp=-70)
        sleep(1.5)
        print(cl.value())
        sleep(0.1)







