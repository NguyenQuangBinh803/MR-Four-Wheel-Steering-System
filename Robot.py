import datetime
import sys
import threading
import time
import serial

class Robot:
    def __init__(self, port, baud_rate):
        try:
            print("Opening serial port: %s..." % port + ".")
            self.robot_serial = serial.Serial(port, baud_rate, timeout=None)
            time.sleep(1)
            self.robot_serial.reset_input_buffer()
            threading.Thread(target=self.flush_data_serial).start()
        except serial.serialutil.SerialException:
            print("Serial not found at port " + port + ".")
            sys.exit(0)

    def flush_data_serial(self):
        self.robot_serial.read(self.robot_serial.in_waiting)
        time.sleep(0.3)

    def write_command(self, cmd):
        cmd = str(cmd)
        print("\t" + str(datetime.datetime.now().time()) + " --- " + "[[  ", cmd, "  ]]")
        self.robot_serial.write(bytes(cmd, 'utf-8'))


DELIMITER = ','
ANGLE_COMMAND = 'q'
SPEED_COMMAND = 'n'
EOF = ';'

if __name__ == "__main__":
    robot = Robot("COM1", 115200)
    front_left_angle = 0
    front_right_angle = 0
    rear_left_angle = 0
    rear_right_angle = 0

    front_left_speed = 0
    front_right_speed = 0
    rear_left_speed = 0
    rear_right_speed = 0

    robot.write_command(
        ANGLE_COMMAND + DELIMITER + str(front_left_angle) + DELIMITER + str(front_right_angle) + DELIMITER + str(
            rear_left_angle) + DELIMITER + str(rear_right_angle) + EOF)
    robot.write_command(
        SPEED_COMMAND + DELIMITER + str(front_left_speed) + DELIMITER + str(front_right_speed) + DELIMITER + str(
            rear_left_speed) + DELIMITER + str(rear_right_speed) + EOF)
