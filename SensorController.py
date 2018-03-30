import time
import json
import grovepi
import RPi.GPIO as gpio
import serial

class SensorController:

    port = "/dev/ttyACM0" #Serial port
    def __init__(self):
        self.gpio.setmode(gpio.BCM)
        self.gpio.setup(25, gpio.IN)

        self.light_pin = 0
        self.sound_pin = 1
        self.dht_pin = 7
        grovepi.pinMode(self.light_pin, "INPUT")
        
        self.s1 = serial.Serial(port, 9600)
        self.s1.flushInput()

    def readSound():
        return self.s1.readline()
    
    def readLight():
        return grovepi.analogRead(self.light_pin)

    def readTemp_Humid():
        return grovepi.dht(dht_pin,0)
    
    def readMotion():
        return gpio.input(25)

    