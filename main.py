from pynvml import *
from time import sleep
import sys
from reprint import output
from tkinter import *
import time


def get_fan_speed(id):
    handle = nvmlDeviceGetHandleByIndex(id)
    return nvmlDeviceGetFanSpeed(handle)


def get_temperature(id):
    handle = nvmlDeviceGetHandleByIndex(id)
    return nvmlDeviceGetTemperature(handle, 0)


def get_memory(id):
    handle = nvmlDeviceGetHandleByIndex(id)
    info = nvmlDeviceGetMemoryInfo(handle)
    return info.used / info.total * 100


def print_each(id):
    print("{:<5}{:<10}{:<10.2f}{:<11}".format(id, get_fan_speed(id), get_memory(id), get_temperature(id)))


nvmlInit()
deviceCount = 3
while (True):
    print('='*40)
    print(time.strftime("%H:%M:%S"))
    print("{:<5}{:<10}{:<10}{:<11}".format('GPU', 'Fan_speed', 'Memory(%)', 'Temperature'))
    for id in range(deviceCount):
        print_each(id)

    sleep(1)
