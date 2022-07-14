import time
from inventor import Inventor2040W, SERVO_1, SERVO_2, SERVO_3, SERVO_4, SERVO_5


# define globals
board = Inventor2040W()

# servos
# arm rotation (base)
servo_armrotate = board.servos[SERVO_1]
servo_armrotate.enable()

# arm pitch at base
servo_armpitch = board.servos[SERVO_2]
servo_armpitch.enable()

# arm bend
servo_armbend = board.servos[SERVO_3]
servo_armbend.enable()

# claw rotation
servo_clawrotate = board.servos[SERVO_4]
servo_clawrotate.enable()

# claw grabber
servo_grab = board.servos[SERVO_5]
servo_grab.enable()
