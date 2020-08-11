import math

# Vehicle sufficient macros
VEL_SCALE = 15
MR_HEIGHT = 30
MR_WIDTH = 48
MR_ANGLE = math.atan(MR_HEIGHT / MR_WIDTH)
MR_DISTANCE_FROM_CENTER = math.sqrt((MR_HEIGHT / 2) * (MR_HEIGHT / 2) + (MR_WIDTH / 2) * (MR_WIDTH / 2))
SCALE = 10
MR_SCALE = 5
CENTER_X = 0
CENTER_Y = 0

# Initailize speed and angle value
front_left_angle = 0
front_right_angle = 0
rear_left_angle = 0
rear_right_angle = 0

front_left_speed = 0
front_right_speed = 0
rear_left_speed = 0
rear_right_speed = 0

# Serial parameters
BAUDRATE = 115200
PORT = "COM1"

# Serial command format
DELIMITER = ','
ANGLE_COMMAND = 'q'
SPEED_COMMAND = 'n'
EOF = ';'

CMD_VEL_SCALE = 200

START_FRAME = "A5"
END_FRAME = "E5"
LENGTH_OF_DATA_RECEIVE = 6