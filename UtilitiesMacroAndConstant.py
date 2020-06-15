from Vehicle import Vehicle
from Robot import Robot
from PVector import PVector
import math
import time
MR_height = 30
MR_width = 48
MR_angle = math.atan(MR_height / MR_width)
MR_distance_from_center = math.sqrt((MR_height / 2) * (MR_height / 2) + (MR_width / 2) * (MR_width / 2))
SCALE = 10

MR_HEIGHT = 30
MR_WIDTH = 48
MR_ANGLE = math.atan(MR_HEIGHT / MR_WIDTH)
MR_DISTANCE_FROM_CENTER = math.sqrt((MR_HEIGHT / 2) * (MR_HEIGHT / 2) + (MR_WIDTH / 2) * (MR_WIDTH / 2))
DELIMITER = ','
ANGLE_COMMAND = 'q'
SPEED_COMMAND = 'n'
EOF = ';'
list_of_point = []


list_of_point.append([ 474.0 , 391.0 ])
#Steering-11.757893 -10.996177 -2.4169683 -2.5146227
list_of_point.append([ 491.0 , 371.0 ])
#Steering-24.556213 -22.314243 -4.720046 -5.976996
list_of_point.append([ 511.0 , 332.0 ])
#Steering-37.9294 -34.341846 -11.292887 -13.628113
list_of_point.append([ 511.0 , 301.0 ])
#Steering-46.21628 -41.977722 -16.535257 -19.453001
list_of_point.append([ 525.0 , 269.0 ])
#Steering-44.481373 -40.514156 -23.24044 -23.13919
list_of_point.append([ 525.0 , 269.0 ])
#Steering-40.587757 -36.859924 -22.36061 -21.510462
list_of_point.append([ 525.0 , 269.0 ])
#Steering-36.212143 -32.61766 -19.347353 -18.223515
list_of_point.append([ 526.0 , 223.0 ])
#Steering-39.91124 -36.582214 -19.2436 -19.637413
list_of_point.append([ 578.0 , 221.0 ])
#Steering-16.912518 -15.391694 -19.472305 -17.958845
list_of_point.append([ 597.0 , 217.0 ])
#Steering-12.189856 -11.163636 -15.956957 -15.065262


# list_of_point.append([ 506.0 , 372.0 ])





CENTER_X = 400
CENTER_Y = 400

BAUDRATE = 115200
PORT = "COM1"

front_left_angle = 0
front_right_angle = 0
rear_left_angle = 0
rear_right_angle = 0

front_left_speed = 0
front_right_speed = 0
rear_left_speed = 0
rear_right_speed = 0
