from data_aquisition import *
from Vehicle import Vehicle
from UtilitiesMacroAndConstant import *
from PVector import PVector


def rounding_angle(angle):
    '''
    Rounding angle make sure it between [-90, 90]
    '''
    # Cover exception returned by atan2 function


    if angle < -270:
        angle += 360
    if angle > 270:
        angle -= 360

    angle = int(angle)

    # Cover min/max
    if angle > 90:
        angle = 90
    elif angle < -90:
        angle = -90

    return angle

if __name__ == "__main__":

    dislocation, angle, cmd_vel, speed_command, steering_command = nav_test_data_aquisition(
        '202007_test_data/20200707_0920_test_result_hardware')

    center_x = 0
    center_y = 0
    vehicle = Vehicle(center_x, center_y, MR_WIDTH / 2)

    # Testcase 1: Validate target point and real point at the beginning
    print('Validate test ==== Before apply displacement')
    print("Target points")
    print(vehicle.front_left_target.x, vehicle.front_left_target.y, vehicle.front_right_target.x,
          vehicle.front_right_target.y)
    print(vehicle.rear_left_target.x, vehicle.rear_left_target.y, vehicle.rear_right_target.x,
          vehicle.rear_right_target.y)

    print("Real points")
    print(vehicle.front_left.x, vehicle.front_left.y, vehicle.front_right.x,
          vehicle.front_right.y)
    print(vehicle.rear_left.x, vehicle.rear_left.y, vehicle.rear_right.x,
          vehicle.rear_right.y)

    # Testcase 2: Validate cmd_vel
    print('Validate test ==== After apply displacement')

    for i, cmd in enumerate(cmd_vel):
        dislocation_vector = PVector.sub2Vectors(vehicle.front_center, vehicle.center)
        # dislocation_vector.setMag(dislocation_vector.mag())

        dislocation_vector.rotate(cmd[1])
        if cmd[0] != 0:
            dislocation_vector.setMag(cmd[0]*10)
        vehicle.follow_vector(dislocation_vector)

        front_left_angle = (vehicle.vel_front_left.heading() - vehicle.temporary_left_frame.heading())* 180 / math.pi
        front_right_angle = (vehicle.vel_front_right.heading() - vehicle.temporary_right_frame.heading())* 180 / math.pi
        rear_left_angle = (vehicle.vel_rear_left.heading() - vehicle.temporary_left_frame.heading())* 180 / math.pi
        rear_right_angle = (vehicle.vel_rear_right.heading() - vehicle.temporary_right_frame.heading())* 180 / math.pi

        front_left_angle = rounding_angle(front_left_angle)
        front_right_angle = rounding_angle(front_right_angle)
        rear_left_angle = rounding_angle(rear_left_angle)
        rear_right_angle = rounding_angle(rear_right_angle)

        if cmd[0] == 0.0:
            continue
        print(angle[i], steering_command[i])
        print(angle[i], front_left_angle , front_right_angle,
              rear_left_angle , rear_right_angle )
