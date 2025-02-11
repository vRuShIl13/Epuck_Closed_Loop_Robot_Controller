import math

# Constants
WHEEL_DIAMETER_MM = 42  # Diameter of the wheel in mm (measured with a ruler)
WHEEL_RADIUS_MM = WHEEL_DIAMETER_MM / 2
AXLE_LENGTH_MM = 53  # Distance between the wheels (measured with a ruler)
STEPS_PER_REVOLUTION = 1000
EPUCK_IP_ADDRESS = "192.168.0.60"
MAX_STEP_COUNT = 2 ** 15

# Helper function 1: Calculate step delta with wraparound
# Handles counter overflow in motor step readings
import math


def steps_delta(last, current, debug=False):
    if debug:
        print("Entering steps_delta")
    delta = current - last
    if delta > MAX_STEP_COUNT // 2:
        delta -= MAX_STEP_COUNT
    elif delta < -MAX_STEP_COUNT // 2:
        delta += MAX_STEP_COUNT
    if debug:
        print(f"Exiting steps_delta with result: {delta}")
    return delta


def calculate_steps_moved(current, start, direction, debug=False):
    if debug:
        print("Entering calculate_steps_moved")
    if direction >= 0:
        if current >= start:
            result = current - start
        else:
            result = (MAX_STEP_COUNT - start) + current
    else:
        if current <= start:
            result = current - start
        else:
            result = (MAX_STEP_COUNT - current) + start
    if debug:
        print(f"Exiting calculate_steps_moved with result: {result}")
    return result


def steps_to_rad(steps, debug=False):
    if debug:
        print("Entering steps_to_rad")
    result = (2 * math.pi * steps) / STEPS_PER_REVOLUTION
    if debug:
        print(f"Exiting steps_to_rad with result: {result}")
    return result


def rad_to_steps(rad, debug=False):
    if debug:
        print("Entering rad_to_steps")
    result = int((rad * STEPS_PER_REVOLUTION) / (2 * math.pi))
    if debug:
        print(f"Exiting rad_to_steps with result: {result}")
    return result


def rad_to_mm(rad, debug=False):
    if debug:
        print("Entering rad_to_mm")
    result = rad * WHEEL_RADIUS_MM
    if debug:
        print(f"Exiting rad_to_mm with result: {result}")
    return result


def mm_to_rad(mm, debug=False):
    if debug:
        print("Entering mm_to_rad")
    result = mm / WHEEL_RADIUS_MM
    if debug:
        print(f"Exiting mm_to_rad with result: {result}")
    return result


def steps_to_mm(steps, debug=False):
    if debug:
        print("Entering steps_to_mm")
    rad = steps_to_rad(steps, debug)
    result = rad_to_mm(rad, debug)
    if debug:
        print(f"Exiting steps_to_mm with result: {result}")
    return result


def mm_to_steps(mm, debug=False):
    if debug:
        print("Entering mm_to_steps")
    rad = mm_to_rad(mm, debug)
    result = rad_to_steps(rad, debug)
    if debug:
        print(f"Exiting mm_to_steps with result: {result}")
    return result


def print_pose(pose, debug=False):
    if debug:
        print("Entering print_pose")
    x_mm, y_mm, theta_rad = pose
    theta_deg = math.degrees(theta_rad)
    print(f"Pose: x={x_mm:.2f} mm, y={y_mm:.2f} mm, theta={theta_deg:.2f}°")
    if debug:
        print("Exiting print_pose")


if __name__ == "__main__":
    last_steps = 200
    current_steps = 500

    print("Step delta:", steps_delta(last_steps, current_steps))
    print("Steps to radians:", steps_to_rad(100))
    print("Radians to steps:", rad_to_steps(math.pi / 2))
    print("Radians to mm:", rad_to_mm(math.pi / 2))
    print("mm to radians:", mm_to_rad(100))
    print("Steps to mm:", steps_to_mm(100))
    print("mm to steps:", mm_to_steps(100))
    print_pose((100, 200, math.pi / 4))
