####################### set/get robot running mode start ###################################################
def set_navigate_mode(self):
    '''
    set robot to navigate mode
    '''
    self.nfc_route = None
    self.__current_mode = NAVIGATE_MODE


def set_linetrace_mode(self):
    '''
    set robot to linetrace mode
    '''
    self.nfc_route = None
    self.__current_mode = LINETRACE_MODE


def set_rimocon_mode(self):
    '''
    set robot to linetrace mode
    '''
    self.nfc_route = None
    self.__current_mode = RIMOCON_MODE


def is_rimocon_mode(self):
    return self.__current_mode == RIMOCON_MODE


def is_linetrace_mode(self):
    '''
    return True if robot is running on linetrace mode, if this method return False it does not mean robot is running on navigate mode

    Using :is_navigate_mode() to check if robot is running on navigate mode
    '''
    return self.__current_mode == LINETRACE_MODE


def is_navigate_mode(self):
    '''
    return True if robot is running on navigate mode, if this method return False it does not mean robot is running on linetrace mode.

    Using :is_linetrace_mode() to check if robot is running on linetrace mode
    '''
    return self.__current_mode == NAVIGATE_MODE


####################### set/get robot running mode end ###################################################
####################### set/get robot status start ###################################################
def set_status_running_slow(self):
    '''
    set robot status to running in slow speed
    '''
    self.__robot_status = ROBOT_STATUS_RUNNING_SLOW


def set_status_stop(self):
    '''
    robot is stopped
    '''
    self.__robot_status = ROBOT_STATUS_STOP


def set_status_rotating(self):
    '''
    robot is rotating
    '''
    self.__robot_status = ROBOT_STATUS_ROTATING


def set_status_running(self):
    '''
    robot is running
    '''
    self.__robot_status = ROBOT_STATUS_RUNNING


def set_status_wait_open_door(self):
    '''
    robot is waiting for door open
    '''
    self.__robot_status = ROBOT_STATUS_WAIT_OPEN_DOOR


def is_status_stop(self):
    '''
    True if robot is stopped
    '''
    return self.__robot_status == ROBOT_STATUS_STOP


def is_status_rotating(self):
    '''
    True if robot is rotating
    '''
    return self.__robot_status == ROBOT_STATUS_ROTATING


def is_status_running(self):
    '''
    True if robot is running
    '''
    return self.__robot_status == ROBOT_STATUS_RUNNING


def is_status_wait_open_door(self):
    '''
    True if robot is running
    '''
    return self.__robot_status == ROBOT_STATUS_WAIT_OPEN_DOOR


def is_allow_receive_command(self):
    '''
    return False if robot is rotating or is waiting for door open
    '''
    return not self.is_status_rotating() and not self.is_status_wait_open_door()


def is_status_running_slow(self):
    '''
    True if robot is running slow
    '''
    return self.__robot_status == ROBOT_STATUS_RUNNING_SLOW


####################### set/get robot status end #####################################################
####################### robot command start ###################################################
def write_command(self, command):
    '''
    Write command to serial
    '''
    command = str(command)
    if command[-1] != common.COMMAND_END:
        command += common.COMMAND_END

    # self.__robot_serial.write(bytes(command, 'utf-8'))


def set_speed_mode(self):
    '''
    Change robot to speed mode
    '''
    # self.write_command(common.COMMAND_CHANGE_TO_SPEED_MODE)
    for _ in range(3):
        self.write_drive_command('start')
        self.write_steer_command('start')
        time.sleep(0.1)


def set_position_mode(self):
    '''
    Change robot to position mode
    '''
    self.write_command(common.COMMAND_CHANGE_TO_POSITION_MODE)


def read_command(self):
    '''
    request robot current position
    '''
    self.write_command("5")
    # bytesRead = self.__robot_serial.inWaiting()
    # return self.__robot_serial.read(bytesRead)


def set_speed(self, speed_data):
    '''
    set speed to robot

    :param speed_data: [front_left_speed, front_right_speed, rear_left_speed, rear_right_speed]
    '''

    command = str(common.COMMAND_DRIVE_4W_INSTANT)
    for speed in speed_data:
        command += common.COMMAND_DELIMITER + str(speed)

    # log(self.root_node, "speed_command", command)
    self.write_command(command)


def set_steering(self, steering_data, is_fast=False):
    '''
    set steering angle to robot

    :param steering_data: [front_left_angle, front_right_angle, rear_left_angle, rear_right_angle]
    '''
    if is_fast:
        command = common.COMMAND_STEER_4W_FAST
    else:
        command = common.COMMAND_STEER_4W_INSTANT

    for steer in steering_data:
        command += common.COMMAND_DELIMITER + str(steer)
    #         # log(self.root_node, "steering_command", command)
    self.write_command(command)


def safe_release(self, attempt_try=3):
    for _ in range(attempt_try):
        self.set_speed([0, 0, 0, 0])
        time.sleep(0.05)


def release_motor(self, param=''):
    '''
    Release motor

    :param param: 0 for release 4 wheels, 1 for release 4 steering, otherwise release all
    '''
    if param is None:
        param = ''
    else:
        param = str(param)
        # if param != '0' and param != '1':
        #     param = ''
    # "x;"
    #         # log(self.root_node, "release motor [" + param + "] => set_speed [0, 0, 0, 0]")
    # self.write_command(str(common.STOP) + common.COMMAND_DELIMITER + param)
    self.set_speed([0, 0, 0, 0])
    time.sleep(0.2)


def set_spin(self, angle, speed=0.5):
    '''
    Spin robot

    :param angle: angle to spin

    :param speed: speed to spin, default is 0.5 km/h
    '''
    command = [str(common.COMMAND_SPIN), str(angle), str(speed)]
    command = common.COMMAND_DELIMITER.join(command)
    # log(self.root_node, command)
    self.write_command(command)


def reset_alarm(self):
    self.write_command(str(common.COMMAND_RESETALARM))


def stop_emergency(self):
    self.set_speed([0, 0, 0, 0])
    time.sleep(0.05)
    self.write_command(str(common.COMMAND_STOP_EMERGENCY))


####################### robot command end ###################################################
####################### robot common function start ###################################################
def rounding_angle(self, angle):
    '''
    Rounding angle make sure it between [-90, 90]
    '''
    # Cover exception returned by atan2 function
    while angle < -270:
        angle += 360
    while angle > 270:
        angle -= 360

    angle = int(angle)

    # Cover min/max
    # if angle > 90:
    #     angle = 90
    # elif angle < -90:
    #     angle = -90

    return angle


def rounding_speed(self, speed):
    '''
    Rounding speed make sure it not greater than MR_MAX_SPEED

    :param speed: speed to rounding in km/h
    '''
    # because 4 wheel will run at 4 different speed
    # if rounding speed, 4 wheel will run at the same speed
    # if speed > MR_MAX_SPEED:
    #     speed = MR_MAX_SPEED
    # elif speed < (-1 * MR_MAX_SPEED):
    #     speed = -1 * MR_MAX_SPEED

    # => 1.4 km/h
    # return format(speed, '.1f')
    if not self.is_navigate_mode():
        return format(speed * self.speed_control.get_accelerator(), '.1f')
    else:
        return format(speed, '.1f')


def reset_linetrace_pid(self):
    self.linetrace_pid_dislocation_angle = 0
    self.linetrace_prev_dislocation_angle = 0
    self.linetrace_curr_time = self.root_node.get_clock().now()
    self.linetrace_prev_time = self.root_node.get_clock().now()


def log_running_status(self):
    status = 'ROBOT STATUS:'
    status += ' Rotating[' + str(self.is_status_rotating()) + ']'
    status += ' Running[' + str(self.is_status_running()) + ']'
    status += ' Running Slow[' + str(self.is_status_running_slow()) + ']'
    status += ' Stop[' + str(self.is_status_stop()) + ']'
    status += ' Wait Door Open[' + str(self.is_status_wait_open_door()) + ']'
    # log(self.root_node, status)


def log_running_mode(self):
    status = 'ROBOT RUNNING MODE:'
    status += ' Linetrace[' + str(self.is_linetrace_mode()) + ']'
    status += ' Navigate[' + str(self.is_navigate_mode()) + ']'
    status += ' Rimocon[' + str(self.is_rimocon_mode()) + ']'
    # log(self.root_node, status)


def slow_down_to_stop(self, time_to_stop=2):
    self.speed_control.slow_down_to_stop(time_to_stop)
    threading.Timer(time_to_stop + 0.1, self.set_status_stop).start()


## New rimocon command for new robot

# Lệnh 2,x; -> Xoay 4 bánh xe
def set_steering_rim(self, steering_angle):
    self.write_steer_command('2,' + str(steering_angle))
    self.write_drive_command('2,' + str(steering_angle))


# Lệnh 3,x; -> Xoay cả xe


# Lệnh 8; -> Stop xe
def set_stop_rim(self):
    self.write_steer_command('8')
    self.write_drive_command('8')


# Lệnh 7,x; -> Xét speed 4 bánh xe km/h
def set_speed_rim(self, speed):
    self.write_steer_command('7,' + str(speed))
    self.write_drive_command('7,' + str(speed))


##Lệnh 0,x; -> Position mode, cho xe chạy x(m)
def set_move_rim(self, distance):
    self.write_steer_command('0,' + str(distance))
    self.write_drive_command('0,' + str(distance))
