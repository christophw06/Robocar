from gpiozero import LineSensor
from time import sleep

sensor = LineSensor(23)

def detected():
    print("Linie erkannt")

def not_detected():
    print("Keine Linie")

sensor.when_line = detected
sensor.when_no_line = not_detected

sleep(3)