from gpiozero import LineSensor
from time import sleep

linesensor_right = LineSensor(23)
linesensor_mid = LineSensor(15)
linesensor_left = LineSensor(14)

def detected_right_line():
    print("Linie erkannt")

def not_detected_right_line():
    print("Keine Linie")
    
def detected_mid_line():
    print("Linie erkannt")

def not_detected_mid_line():
    print("Keine Linie")
    
def detected_left_line():
    print("Linie erkannt")

def not_detected_left_line():
    print("Keine Linie")

linesensor_right.when_line = detected_right_line
linesensor_right.when_no_line = not_detected_right_line

linesensor_mid.when_line = detected_mid_line
linesensor_mid.when_no_line = not_detected_mid_line

linesensor_left.when_line = detected_left_line
linesensor_left.when_no_line = not_detected_left_line

sleep(3)