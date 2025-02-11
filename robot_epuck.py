# robot_epuck.py
import time

from Helper.epuck_com import EPuckCom
from Helper.epuck_ip import EPuckIP
from robot import Robot


class RobotEPuck(Robot):
    def __init__(self, ip_address = 0, comm = "" ):
        super().__init__()
        self.ip_address = ip_address
        self.epuckcomm = comm

    def setup(self):
        print(f"Connecting to e-puck at {self.ip_address}...")
        if self.ip_address == 0:
            self.epuckcomm = EPuckCom(self.epuckcomm, debug=False)
        else:
            self.epuckcomm = EPuckIP(self.ip_address, debug=True)
        if not self.epuckcomm.connect():
            print("Failed to connect to e-puck.")
            return

        self.epuckcomm.enable_sensors = True
        self.epuckcomm.send_command()  # Enable sensor stream
        time.sleep(0.3)  # Wait for the robot to process the request
        print("e-puck setup complete.")

    def update(self):
        self.epuckcomm.data_update()  # Update sensor data
        # Add any commands here to control the robot if needed

    def terminate(self):
        print("Terminating e-puck connection...")
        self.epuckcomm.stop_all()
        self.epuckcomm.close()
        print("e-puck connection closed.")
    #reset pose
    def odom_reset(self):
        self.robot_pose = (0, 0, 0)
        print("Odometry reset to (0, 0, 0).")

    #update the pose
    def odom_update(self):
        left_steps = self.epuckcomm.state.sens_left_motor_steps
        right_steps = self.epuckcomm.state.sens_right_motor_steps
        self.robot_pose = self.calculate_odometry(left_steps, right_steps)
        print(f"Updated odometry: {self.robot_pose}")

    def calculate_odometry(self, left_steps, right_steps):
        # Replace with your actual odometry calculation logic
        return 0, 0, 0

    # get sensor data like proximity and ground
