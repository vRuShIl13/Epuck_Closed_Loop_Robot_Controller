import time


class Controller:
    def __init__(self):
        self.planner = None
        self.navigator = None
        self.robot = None
        self.target_hz = 10
        self.running = False

    def setup(self, planner, navigator, robot, hz=10):

        self.planner = planner
        self.navigator = navigator
        self.robot = robot
        self.target_hz = hz

        planner.controller = self
        navigator.controller = self
        robot.controller = self

        planner.setup()
        navigator.setup()
        robot.setup()

    def start(self):
        self.running = True
        loop_interval = 1.0 / self.target_hz

        print("Controller started. Running at", self.target_hz, "Hz.")
        try:
            while self.running:
                start_time = time.time()

                if not self.planner.update():
                    self.running = False
                self.navigator.update()
                self.robot.update()

                time.sleep(loop_interval)

        except KeyboardInterrupt:
            print("\nController interrupted by user.")

    def terminate(self):
        print("Terminating controller and modules...")
        self.planner.terminate()
        self.navigator.terminate()
        self.robot.terminate()
        print("Controller terminated.")
