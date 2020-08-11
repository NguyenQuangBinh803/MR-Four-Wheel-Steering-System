import serial
import time
from datetime import datetime
import sys
from UtilitiesMacroAndConstant import *
import numpy as np

class RobotControl:

    def __init__(self, port, baud_rate):

        self.logging = open("GM6020_test_result/" + datetime.now().strftime("%Y%m%d_%H%M%S_") + ".txt", "w")
        ports = port.split(',')
        try:
            self.logging.write("[Openning_serial]")
            print(ports[0], ports[1])
            self.__robot_serial_steer = serial.Serial(ports[0], baud_rate, timeout=None)
            self.__robot_serial_drive = serial.Serial(ports[1], baud_rate, timeout=None)
            time.sleep(0.5)

            self.__robot_serial_steer.reset_input_buffer()
            self.__robot_serial_drive.reset_input_buffer()
            time.sleep(0.1)

        except serial.serialutil.SerialException as exp:
            self.logging.write("[serial_port]" + str(ports))
            sys.exit(str(exp))

    def flush_data_serial(self):
        # self.__robot_serial.read(self.__robot_serial.in_waiting)
        self.__robot_serial_steer.read(self.__robot_serial_steer.in_waiting)
        self.__robot_serial_drive.read(self.__robot_serial_drive.in_waiting)
        time.sleep(0.1)

    def write_spin_command(self, spin_angle):
        if abs(self.rimocon_current_angle) != abs(spin_angle):
            self.rimocon_current_angle = spin_angle
            self.write_steer_command('4')
            self.write_drive_command('4')
            time.sleep(1.5)
        self.write_steer_command('3,' + str(spin_angle))
        self.write_drive_command('3,' + str(spin_angle))

    def read_command(self):
        '''
        request robot current position
        '''
        self.__robot_serial_drive.write("5;".encode("utf-8"))
        bytesRead = self.__robot_serial_drive.inWaiting()
        return self.__robot_serial_drive.read(bytesRead)

    def convert_string_to_int32(self, strData):
        return (np.int32(strData[0]) << 24) + (np.int32(strData[1]) << 16) + (np.int32(strData[2]) << 8) + (
            np.int32(strData[3]))

    def get_dislocation(self):
        raw_data = str(self.read_command(), 'utf-8').split()

        # Check length of receive buffer with start and end frame
        if (len(raw_data) == LENGTH_OF_DATA_RECEIVE and raw_data[0] == START_FRAME and raw_data[-1] == END_FRAME):
            receive_data = raw_data[1:-1]
        else:
            return []

        distance_front_left = self.convert_string_to_int32(receive_data[1:5])
        distance_front_right = self.convert_string_to_int32(receive_data[6:10])
        distance_rear_left = self.convert_string_to_int32(receive_data[11:15])
        distance_rear_right = self.convert_string_to_int32(receive_data[16:])
        return distance_front_left, distance_front_right, distance_rear_left, distance_rear_right

    def write_steer_command(self, command):
        '''
        Write command to serial
        '''
        command = str(command)
        if command[-1] != EOF:
            command += EOF
        print(command)
        self.logging.write("[write_steer_command]" + command + "\n")
        self.__robot_serial_steer.write(command.encode('utf-8'))
    
    def write_drive_command(self, command):
        '''
        Write command to serial
        '''
        command = str(command)
        if command[-1] != EOF:
            command += EOF
        print(command)
        self.logging.write("[write_drive_command]" + command + "\n")
        self.__robot_serial_drive.write(command.encode('utf-8'))

if __name__ == "__main__":

    print("Testing robot full function")
    robot = RobotControl("/dev/ttyUSB1,/dev/ttyUSB0", 115200)

    while True:
        robot.write_steer_command("q,45,45,-45,-45")
        robot.write_drive_command("n,1,1,1,1")
        print(robot.get_dislocation())
        time.sleep(0.1)




