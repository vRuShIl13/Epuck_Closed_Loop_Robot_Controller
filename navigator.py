from abc import ABC, abstractmethod

class Navigator(ABC):
    def __init__(self):
        self.controller = None
        self.has_hit_target = False

    @abstractmethod
    def setup(self):

        pass

    @abstractmethod
    def update(self):

        pass

    @abstractmethod
    def terminate(self):

        pass

    @abstractmethod
    def set_target(self, target):

        pass
