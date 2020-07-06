from data_aquisition import *
from Vehicle import Vehicle
from UtilitiesMacroAndConstant import *
from PVector import PVector

if __name__ == "__main__":

    dislocation, angle, cmd_vel, speed_command, steering_command = nav_test_data_aquisition('202007_test_data/20200704_1207_test_result_hardware')
    
    center_x = 0
    center_y = 0
    vehicle = Vehicle(center_x, center_y, MR_WIDTH / 2)

    # print(vehicle.rear_center_target.x, vehicle.rear_center_target.y, vehicle.front_center_target.x,
    #       vehicle.front_center_target.y)

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

    print('Validate test ==== After apply displacement')
    # vehicle.follow(224.0, 158.0)
    
    for cmd in cmd_vel:
        dislocation_vector = PVector.sub2Vectors(vehicle.front_center, vehicle.center)

        # print(dislocation_vector.mag(), cmd[0])
        dislocation_vector.setMag(cmd[0]*60)
        dislocation_vector.rotate(cmd[1])
        vehicle.follow_vector(dislocation_vector)
        
        print(vehicle.vel_front_left.heading()*180/math.pi, vehicle.vel_front_right.heading()*180/math.pi, vehicle.vel_rear_left.heading()*180/math.pi, vehicle.vel_rear_right.heading()*180/math.pi)
        # print()
        