import motor
import sensor
import time

motor.init()

def stop_all_wheels():
    motor.front_left(0)
    motor.front_right(0)
    motor.rear_left(0)
    motor.rear_right(0)

def turn_right(turn_speed, turn_radius):
    wheelbase_in_cm= 13
    right_wheel_speed=0
    left_wheel_speed=0
    turn_radius_scaled= turn_radius*0.1
    if 0< turn_radius_scaled <=10 and 0< turn_speed <=100:
        right_wheel_speed= int(((turn_speed * ((turn_radius_scaled + wheelbase_in_cm/2)/turn_radius_scaled ))/330)*100)
        left_wheel_speed= int(((turn_speed * ((turn_radius_scaled - wheelbase_in_cm/2)/turn_radius_scaled ))/330)*100)

    motor.front_left(left_wheel_speed)
    motor.front_right(right_wheel_speed)
    motor.rear_left(left_wheel_speed)
    motor.rear_right(right_wheel_speed)

def turn_left(turn_speed, turn_radius):
    wheelbase_in_cm= 13
    right_wheel_speed=0
    left_wheel_speed=0
    turn_radius_scaled= turn_radius*0.1
    if 0< turn_radius_scaled <=10 and 0< turn_speed <=100:
        right_wheel_speed= int(((turn_speed * ((turn_radius_scaled - wheelbase_in_cm/2)/turn_radius_scaled ))/330)*100)
        left_wheel_speed=  int(((turn_speed * ((turn_radius_scaled + wheelbase_in_cm/2)/turn_radius_scaled ))/330)*100)

    motor.front_left(left_wheel_speed)
    motor.front_right(right_wheel_speed)
    motor.rear_left(left_wheel_speed)
    motor.rear_right(right_wheel_speed)



time.sleep(3)
stop_all_wheels()
