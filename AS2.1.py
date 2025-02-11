import controller
import navigator
import navigator_diff_simple
import planner
import planner_move_once
import robot
import robot_epuck
import math

robot = robot_epuck.RobotEPuck("COM9")
planner = planner_move_once.PlannerMoveOnce((300, 1, math.pi/2))
navigator = navigator_diff_simple.NavigatorDiffSimple()
controller = controller.Controller()
controller.setup(planner, navigator, robot)
controller.start() #blocking until done
controller.terminate()
print("Controller exited")
