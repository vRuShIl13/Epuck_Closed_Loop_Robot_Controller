import math
from epuck_helper_functions import steps_to_mm
from epuck_helper_functions import AXLE_LENGTH_MM
import numpy as np


# Task 2:  Open Loop Forward Kinematics
def diff_drive_forward_kin(pose, left_steps, right_steps, debug=False):
    """
    Compute the new pose of the robot after wheel movements using forward kinematics.

    Args:
        pose: Tuple (x, y, theta), current robot pose in mm and radians.
        left_steps: Number of steps moved by the left wheel.
        right_steps: Number of steps moved by the right wheel.
        debug: Boolean, if True, prints debug information.

    Returns:
        Tuple (new_x, new_y, new_theta), new robot pose.
    """
    if debug:
        print("Entering diff_drive_forward_kin")

    x, y, theta = pose

    # Convert steps to distances
    d_left = steps_to_mm(left_steps, debug)
    d_right = steps_to_mm(right_steps, debug)

    # Calculate linear and angular displacement
    delta_d = (d_left + d_right) / 2
    delta_theta = (d_right - d_left) / AXLE_LENGTH_MM

    # Update pose
    if abs(delta_theta) > 1e-6:  # Robot is turning
        radius = delta_d / delta_theta
        new_x = x + radius * (math.sin(theta + delta_theta) - math.sin(theta))
        new_y = y - radius * (math.cos(theta + delta_theta) - math.cos(theta))
    else:  # Robot is moving straight
        new_x = x + delta_d * math.cos(theta)
        new_y = y + delta_d * math.sin(theta)

    new_theta = (theta + delta_theta) % (2 * math.pi)  # Normalize theta

    if debug:
        print("Exiting diff_drive_forward_kin")

    return new_x, new_y, new_theta


if __name__ == "__main__":
    test_cases = [
        # Each case contains initial_pose, left_steps, right_steps, and the expected result
        ((0, 0, 0), 0, 0, (0, 0, 0)),
        ((10, 20, 0), 1290, 1290, (178, 20, 0)),
        ((10, 20, np.pi / 2), 1290, 1290, (10, 188, 90)),
        ((0, 0, 0), -1290, 1290, (0, 0, 0)),
        ((0, 0, np.pi / 2), 1290, -1290, (0, 0, 90)),
        ((0, 0, 0), 2580, 0, (0, 0, 0)),
        ((1000, 1000, np.pi / 2), 1290, -1290, (1000, 1000, 90)),
        ((0, 0, np.pi / 2), 1290, 100, (62, 7, 283)),
        ((0, 0, 0), 1991, 2075, (263, 27, 12)),
        ((0, 0, 0), 189, 2422, (-23, 10, 312)),
        ((0, 0, 0), 1249, 2598, (-11, 152, 188)),
    ]

    for initial_pose, left_steps, right_steps, expected in test_cases:
        new_pose = diff_drive_forward_kin(initial_pose, left_steps, right_steps)
        print(f"Left steps: {left_steps}, Right steps: {right_steps}")
        print(f"New pose: x={new_pose[0]:.2f} mm, y={new_pose[1]:.2f} mm, theta={math.degrees(new_pose[2]):.2f}°")
        print(f"Expected: x={expected[0]:.2f} mm, y={expected[1]:.2f} mm, theta={expected[2]:.2f}°\n")
