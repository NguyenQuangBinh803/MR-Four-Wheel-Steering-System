from UtilitiesMacroAndConstant import *

def check_distance(a, b, check):
  return check < PVector.sub2Vectors(a,b).mag()


if __name__ == "__main__":
    vehicle = Vehicle(CENTER_X, CENTER_Y, MR_WIDTH / 2)
    robot = Robot(PORT, BAUDRATE)
    for point in list_of_point:
        # while(check_distance(vehicle.center, PVector(point[0], point[1]), 0.1)):
        vehicle.follow(point[0], point[1])

        front_left_angle = vehicle.steering_front_left * 180 / math.pi
        front_right_angle = vehicle.steering_front_right * 180 / math.pi
        rear_left_angle = vehicle.steering_rear_left * 180 / math.pi
        rear_right_angle = vehicle.steering_rear_right * 180 / math.pi

        front_left_speed = vehicle.vel_front_left.mag()
        front_right_speed = vehicle.vel_front_right.mag()
        rear_left_speed = vehicle.vel_rear_left.mag()
        rear_right_speed = vehicle.vel_rear_right.mag()


        print("Velocity")
        print(front_left_speed, front_right_speed, rear_left_speed, rear_right_speed)
        print("Steering")
        print(front_left_angle, front_right_angle, rear_left_angle, rear_right_angle)

        # robot.write_command(
        #     ANGLE_COMMAND + DELIMITER + str(front_left_angle) + DELIMITER + str(front_right_angle) + DELIMITER + str(
        #         rear_left_angle) + DELIMITER + str(rear_right_angle) + EOF)
        # robot.write_command(
        #     SPEED_COMMAND + DELIMITER + str(front_left_speed) + DELIMITER + str(front_right_speed) + DELIMITER + str(
        #         rear_left_speed) + DELIMITER + str(rear_right_speed) + EOF)




