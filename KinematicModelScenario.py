from UtilitiesMacroAndConstant import *
from Vehicle import Vehicle
from Robot import Robot
import time

from testcase_3 import *

if __name__ == "__main__":
    vehicle = Vehicle(CENTER_X, CENTER_Y, MR_WIDTH / 2)
    robot = Robot(PORT, BAUDRATE)
    robot.write_command('V,;')
    robot.write_command('n,0,0,0,0;')
    time.sleep(0.5)
    for point in list_of_point:
        vehicle.follow(point[0], point[1])

        front_left_angle = (vehicle.vel_front_left.heading() - vehicle.temporary_left_frame.heading()) * 180 / math.pi
        front_right_angle = (vehicle.vel_front_right.heading() - vehicle.temporary_right_frame.heading()) * 180 / math.pi
        rear_left_angle = (vehicle.vel_rear_left.heading() - vehicle.temporary_left_frame.heading()) * 180 / math.pi
        rear_right_angle = (vehicle.vel_rear_right.heading() - vehicle.temporary_right_frame.heading()) * 180 / math.pi

        front_left_speed = vehicle.vel_front_left.mag() / VEL_SCALE
        front_right_speed = vehicle.vel_front_right.mag() / VEL_SCALE
        rear_left_speed = vehicle.vel_rear_left.mag() / VEL_SCALE
        rear_right_speed = vehicle.vel_rear_right.mag() / VEL_SCALE

        # Cover exception returned by atan2 function
        if (front_left_angle < -270):
            front_left_angle += 360
        if (front_right_angle < -270):
            front_right_angle += 360
        if (rear_left_angle < -270):
            rear_left_angle += 360
        if (rear_right_angle < -270):
            rear_right_angle += 360

        if (front_left_angle > 270):
            front_left_angle -= 360
        if (front_right_angle > 270):
            front_right_angle -= 360
        if (rear_left_angle > 270):
            rear_left_angle -= 360
        if (rear_right_angle > 270):
            rear_right_angle -= 360
        # =======================================================

        print("Velocity")
        print(front_left_speed, front_right_speed, rear_left_speed, rear_right_speed)
        print("Steering")
        print(front_left_angle, front_right_angle, rear_left_angle, rear_right_angle)

        robot.write_command(
            ANGLE_COMMAND + DELIMITER + str(int(front_left_angle)) + DELIMITER + str(
                int(front_right_angle)) + DELIMITER + str(
                int(rear_left_angle)) + DELIMITER + str(int(rear_right_angle)) + EOF)
        robot.write_command(
            SPEED_COMMAND + DELIMITER + str(front_left_speed) + DELIMITER + str(front_right_speed) + DELIMITER + str(
                rear_left_speed) + DELIMITER + str(rear_right_speed) + EOF)

        time.sleep(0.2)
    robot.write_command('n,0,0,0,0;')
