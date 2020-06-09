from Vehicle import Vehicle
from Robot import Robot
from PVector import PVector
import math
from time import *

MR_HEIGHT = 100
MR_WIDTH = 200
MR_ANGLE = math.atan(MR_HEIGHT / MR_WIDTH)
MR_DISTANCE_FROM_CENTER = math.sqrt((MR_HEIGHT / 2) * (MR_HEIGHT / 2) + (MR_WIDTH / 2) * (MR_WIDTH / 2))
DELIMITER = ','
ANGLE_COMMAND = 'q'
SPEED_COMMAND = 'n'
EOF = ';'
list_of_point = []

list_of_point.append([ 548.0 , 400.0 ])
list_of_point.append([ 588.0 , 401.0 ])
list_of_point.append([ 618.0 , 403.0 ])
list_of_point.append([ 648.0 , 409.0 ])
list_of_point.append([ 659.0 , 428.0 ])
list_of_point.append([ 671.0 , 447.0 ])
list_of_point.append([ 684.0 , 479.0 ])
list_of_point.append([ 687.0 , 506.0 ])
list_of_point.append([ 682.0 , 544.0 ])
list_of_point.append([ 669.0 , 569.0 ])
list_of_point.append([ 649.0 , 590.0 ])
list_of_point.append([ 632.0 , 605.0 ])
list_of_point.append([ 619.0 , 624.0 ])
list_of_point.append([ 600.0 , 629.0 ])
list_of_point.append([ 584.0 , 644.0 ])
list_of_point.append([ 567.0 , 658.0 ])
list_of_point.append([ 539.0 , 668.0 ])
list_of_point.append([ 497.0 , 679.0 ])
list_of_point.append([ 474.0 , 684.0 ])
list_of_point.append([ 428.0 , 693.0 ])



# list_of_point.append([505.0, 375.0])
# list_of_point.append([513.0, 369.0])
# list_of_point.append([513.0, 369.0])
# list_of_point.append([513.0, 369.0])
# list_of_point.append([513.0, 369.0])
# list_of_point.append([513.0, 369.0])
# list_of_point.append([513.0, 369.0])
# list_of_point.append([513.0, 369.0])
# list_of_point.append([513.0, 369.0])
# list_of_point.append([513.0, 369.0])
# list_of_point.append([513.0, 369.0])
# list_of_point.append([513.0, 369.0])
# list_of_point.append([524.0, 359.0])
# list_of_point.append([540.0, 354.0])
# list_of_point.append([541.0, 354.0])
# list_of_point.append([542.0, 354.0])
# list_of_point.append([561.0, 355.0])
# list_of_point.append([562.0, 355.0])
# list_of_point.append([567.0, 357.0])
# list_of_point.append([570.0, 357.0])
# list_of_point.append([571.0, 357.0])
# list_of_point.append([574.0, 358.0])
# list_of_point.append([576.0, 358.0])
# list_of_point.append([578.0, 359.0])
# list_of_point.append([585.0, 362.0])
# list_of_point.append([586.0, 363.0])
# list_of_point.append([588.0, 366.0])
# list_of_point.append([590.0, 368.0])
# list_of_point.append([593.0, 371.0])
# list_of_point.append([594.0, 373.0])
# list_of_point.append([601.0, 380.0])
# list_of_point.append([605.0, 386.0])
# list_of_point.append([606.0, 389.0])
# list_of_point.append([608.0, 396.0])
# list_of_point.append([608.0, 397.0])
# list_of_point.append([608.0, 397.0])
# list_of_point.append([609.0, 398.0])
# list_of_point.append([636.0, 405.0])
# list_of_point.append([636.0, 405.0])
# list_of_point.append([639.0, 406.0])
# list_of_point.append([639.0, 406.0])
# list_of_point.append([642.0, 407.0])
# list_of_point.append([644.0, 408.0])
# list_of_point.append([646.0, 410.0])
# list_of_point.append([650.0, 414.0])
# list_of_point.append([651.0, 416.0])
# list_of_point.append([652.0, 419.0])
# list_of_point.append([653.0, 422.0])
# list_of_point.append([665.0, 432.0])
# list_of_point.append([667.0, 437.0])
# list_of_point.append([670.0, 443.0])
# list_of_point.append([671.0, 446.0])
# list_of_point.append([671.0, 452.0])
# list_of_point.append([671.0, 457.0])
# list_of_point.append([671.0, 462.0])
# list_of_point.append([673.0, 469.0])
# list_of_point.append([683.0, 480.0])
# list_of_point.append([685.0, 494.0])
# list_of_point.append([685.0, 497.0])
# list_of_point.append([685.0, 502.0])
# list_of_point.append([684.0, 507.0])
# list_of_point.append([684.0, 510.0])
# list_of_point.append([684.0, 510.0])
# list_of_point.append([684.0, 511.0])
# list_of_point.append([684.0, 515.0])
# list_of_point.append([684.0, 520.0])
# list_of_point.append([683.0, 523.0])
# list_of_point.append([680.0, 528.0])
# list_of_point.append([677.0, 541.0])
# list_of_point.append([674.0, 547.0])
# list_of_point.append([674.0, 551.0])
# list_of_point.append([674.0, 555.0])
# list_of_point.append([673.0, 560.0])
# list_of_point.append([670.0, 571.0])
# list_of_point.append([668.0, 577.0])
# list_of_point.append([665.0, 583.0])
# list_of_point.append([662.0, 590.0])
# list_of_point.append([659.0, 595.0])
# list_of_point.append([657.0, 600.0])
# list_of_point.append([653.0, 607.0])
# list_of_point.append([653.0, 607.0])
# list_of_point.append([652.0, 610.0])
# list_of_point.append([652.0, 612.0])
# list_of_point.append([652.0, 615.0])
# list_of_point.append([652.0, 615.0])
# list_of_point.append([652.0, 615.0])
# list_of_point.append([652.0, 615.0])
# list_of_point.append([652.0, 615.0])
# list_of_point.append([652.0, 616.0])
# list_of_point.append([652.0, 617.0])
# list_of_point.append([652.0, 617.0])
# list_of_point.append([653.0, 618.0])
# list_of_point.append([656.0, 618.0])
# list_of_point.append([656.0, 618.0])
# list_of_point.append([667.0, 621.0])
# list_of_point.append([677.0, 622.0])
# list_of_point.append([681.0, 622.0])
# list_of_point.append([681.0, 622.0])
# list_of_point.append([681.0, 622.0])
# list_of_point.append([681.0, 622.0])
# list_of_point.append([682.0, 622.0])
# list_of_point.append([696.0, 628.0])
# list_of_point.append([696.0, 628.0])

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
