import re

DEBUG_MODE = False


def nav_test_data_aquisition(filename):
    '''

    :param filename:
    :return:
    '''
    dislocation = []
    cmd_vel = []
    angle = []
    speed_command = []
    steering_command = []

    f = open(filename)
    p = re.compile(r'\d+\.\d+')
    integer = re.compile(r'\d+')
    for line in f:
        string = re.search("mix]:(.*)", line)
        if string:

            dislocate = re.search("Dislocation ](.*)", string.group(1))
            if dislocate:
                dislocation.append(p.findall(dislocate.group(1)))
            time = re.search("time](.*)Time", string.group(1))

            if time:
                angle.append(p.findall(time.group(1)))
            modulus = re.search("vel_modulus](.*)", string.group(1))

            if modulus:
                cmd_vel.append(p.findall(modulus.group(1)))
            speed_command_string = re.search("n,(.*)", string.group(1))
            steer_command_string = re.search("q,(.*)", string.group(1))

            if speed_command_string:
                if len(integer.findall(speed_command_string.group(1))) > 4:
                    speed_command.append(p.findall(speed_command_string.group(1)))
                else:
                    speed_command.append(integer.findall(speed_command_string.group(1)))

            if steer_command_string:
                print(steer_command_string.group(1))
                if len(integer.findall(steer_command_string.group(1))) > 4:
                    steering_command.append(p.findall(steer_command_string.group(1)))
                else:
                    steering_command.append(integer.findall(steer_command_string.group(1)))
            # print(string.group(1))

    # Convert str data to float
    steering_command = [[float(y) for y in x] for x in steering_command]
    cmd_vel = [[float(y) for y in x] for x in cmd_vel]

    return dislocation, angle, cmd_vel, speed_command, steering_command

if __name__ == "__main__":
    # dislocation, angle, cmd_vel, speed_command, steering_command = nav_test_data_aquisition('202007_test_data/20200704_1207_test_result_hardware')
    dislocation, angle, cmd_vel, speed_command, steering_command = nav_test_data_aquisition('202007_test_data/20200708_1100_test_result_hardware')


    # Unit test
    # for steer in steering_command:
    #     print(steer, type(steer[0]))
    # for steer in speed_command:
    #     print(steer, type(steer[0]))
    # for cmd in cmd_vel:
    #     print(cmd)
    # for ang in angle:
    #     print(ang)
    # for dis in dislocation:
    #     print(dis, type(dis[0]))

    
    # steering_command = [float(i) for i in steering_command]
    # steering_command = [float(i) for i in steering_command]

    for i in range(len(steering_command)):
        print(dislocation[i])
        if cmd_vel[i][0] == 0.0 and cmd_vel[i][1] != 0.0:

            print(cmd_vel[i], "\tNavigation is spinning")
        elif cmd_vel[i][0] == 0.0 and cmd_vel[i][1] == 0.0:
            print(cmd_vel[i], "\tNavigation is stopped")
        elif cmd_vel[i][0] != 0.0 and cmd_vel[i][1] != 0.0:
            print(cmd_vel[i], "\tNavigation is running")
