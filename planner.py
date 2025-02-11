from abc import ABC, abstractmethod


class Planner(ABC):
    def __init__(self):
        self.controller = None

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def update(self):
        # Return True if still running, False if done planning
        pass

    @abstractmethod
    def terminate(self):
        pass
