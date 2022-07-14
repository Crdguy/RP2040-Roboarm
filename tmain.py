import time
from inventor import Inventor2040W, SERVO_1
from math import atan

# define globals
board = Inventor2040W()
servo1 = board.servos[SERVO_1]
servo1.enable()

x = ADC(26)
y = ADC(27)


def incremental():
    while True:
        t = 0
        deg = 0
        while t <= 5:
            deg = 2**(1.7*t)
            print("deg: " + str(deg))
            servo1.to_percent(deg/360)
            t = t + 0.01
            time.sleep(0.01)


def joystick_control():
    while True:
        x_num = x.read_u16()/65535 - 0.5
        y_num = y.read_u16()/65535 - 0.5
        print("X: {}\nY: {}\n---".format(x_num, y_num))
        servo1.to_percent(atan(y_num/x_num))
        
        time.sleep(0.05)
