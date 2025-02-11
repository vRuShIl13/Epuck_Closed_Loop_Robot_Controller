import numpy as np
from epuck_helper_functions import AXLE_LENGTH_MM, mm_to_steps


# Task 4: Inverse Kinematics
def diff_drive_inverse_kin(distance_mm, speed_mm_s, omega_rad, debug=False):
    """
    :param distance_mm: Distance to be travelled (mm)
    :param speed_mm_s: Signed speed (mm/s), negative if moving backwards
    :param omega_rad: Angle of turn (radians)
    :param debug: Boolean, if True, prints debug information
    :return: left wheel speed (steps), right wheel speed (steps), total left steps, total right steps
    """
    if debug:
        print("Entering diff_drive_inverse_kin")

    angular_velocity_rad = 0
    axle_radius = AXLE_LENGTH_MM / 2

    if distance_mm == 0:
        angular_velocity_rad = abs(speed_mm_s) / axle_radius
        left_distance_mm = -omega_rad * axle_radius
        right_distance_mm = omega_rad * axle_radius

        left_speed_mm = -angular_velocity_rad * axle_radius if omega_rad > 0 else angular_velocity_rad * axle_radius
        right_speed_mm = angular_velocity_rad * axle_radius if omega_rad > 0 else -angular_velocity_rad * axle_radius
    else:
        time_s = abs(distance_mm / speed_mm_s)
        if time_s != 0:
            angular_velocity_rad = omega_rad / time_s

        omega_axle_half = omega_rad * axle_radius
        distance_abs = abs(distance_mm)

        left_speed_mm = speed_mm_s - angular_velocity_rad * axle_radius
        right_speed_mm = speed_mm_s + angular_velocity_rad * axle_radius

        left_distance_mm = distance_abs - omega_axle_half if omega_rad >= 0 else distance_abs + omega_axle_half
        right_distance_mm = distance_abs + omega_axle_half if omega_rad >= 0 else distance_abs - omega_axle_half

    left_speed_steps = mm_to_steps(left_speed_mm)
    right_speed_steps = mm_to_steps(right_speed_mm)
    left_steps = mm_to_steps(left_distance_mm)
    right_steps = mm_to_steps(right_distance_mm)

    if debug:
        print("Exiting diff_drive_inverse_kin")

    return left_speed_steps, right_speed_steps, left_steps, right_steps


if __name__ == "__main__":
    test_cases = [
        (130, 10, 0, (75, 75, 978, 978)),
        (130, -10, 0, (-75, -75, 978, 978)),
        (300, 50, 0, (376, 376, 2257, 2257)),
        (200, 70, np.pi / 4, (472, 582, 1348, 1661)),
        (-200, 70, np.pi / 4, (472, 582, 1348, 1661)),
        (300, -40, -np.pi * 2, (-134, -468, 1005, 3510)),
        (0, 100, -np.pi * 2, (753, -753, 1253, -1253)),
        (0, 50, np.pi / 2, (-376, 376, -313, 313)),
        (0, -50, np.pi / 2, (-376, 376, -313, 313))
    ]

    for idx, (distance, speed, omega, expected) in enumerate(test_cases, 1):
        actual = diff_drive_inverse_kin(distance, speed, omega)
        print(f"Test Case #{idx}:")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}\n")
