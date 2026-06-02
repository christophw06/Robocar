import sensor
import time

def get_value_sensor_in_list(sensor_value, readin_timestep_in_ms, number_of_values_to_readin):
    values=[]
    number_of_values= len(values)
    while True:
        if sensor_value:
            sensor_value_converted = 1
        else:
            sensor_value_converted = 0

        if number_of_values < number_of_values_to_readin:
            values.append(sensor_value_converted)
            time.sleep((readin_timestep_in_ms/number_of_values_to_readin)/100)
        elif number_of_values >= number_of_values_to_readin:
            del values[0]
            values.append(sensor_value_converted)
            time.sleep((readin_timestep_in_ms/number_of_values_to_readin)/100)

        return values


def average_value(values_list):
    number_to_divide= len(values_list)
    average_value= sum(values_list)/number_to_divide

while True:
    print = average_value(get_value_sensor_in_list(sensor.sensor_line("mid"), 200, 10))
