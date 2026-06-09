import queue
import threading

import logic
import motor
import sensor

motor.init()


def stop_all_wheels():
    motor.front_left(0)
    motor.front_right(0)
    motor.rear_left(0)
    motor.rear_right(0)


def drive_in_direction(speed_left, speed_right, threshold_rear_steering):
    while True:
        get_speed_input_left = speed_left.get()
        get_speed_input_right = speed_right.get()
        if (
            0 < abs(get_speed_input_left) <= 100
            and 0 <= abs(get_speed_input_right) <= 100
        ):
            right_wheel_speed = int(get_speed_input_right)
            left_wheel_speed = int(get_speed_input_left)

        diff_right_left_speed = right_wheel_speed - left_wheel_speed

        if diff_right_left_speed > threshold_rear_steering:
            rear_speed_right = right_wheel_speed
            rear_speed_left = -left_wheel_speed
        elif diff_right_left_speed > -threshold_rear_steering:
            rear_speed_right = -right_wheel_speed
            rear_speed_left = left_wheel_speed
        else:
            rear_speed_right = right_wheel_speed
            rear_speed_left = left_wheel_speed

        motor.front_left(left_wheel_speed)
        motor.front_right(right_wheel_speed)
        motor.rear_left(rear_speed_left)
        motor.rear_right(rear_speed_right)


drive_test = threading.Thread(
    target=drive_in_direction,
    args=(
        logic.speed_left_wheel,
        logic.speed_right_wheel,
        sensor.config_data["hard_turning_threshold"],
    ),
)

drive_test.start()
