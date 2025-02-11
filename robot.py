# robot.py
from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self):
        self.controller = None
        self.state = None
        self.robot_pose = (0, 0, 0)

    @abstractmethod
    def setup(self):
        # initial setup
        pass

    @abstractmethod
    def update(self):
        # updating the robot
        pass

    @abstractmethod
    def terminate(self):
        # close everything
        pass
    @abstractmethod
    def odom_reset(self):
        # reset pose as 0, 0, 0
        pass
    @abstractmethod
    def odom_update(self):
        # odom update
        pass
