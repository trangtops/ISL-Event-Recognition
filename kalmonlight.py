import math
import matplotlib
matplotlib.use("Pdf")
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
import numpy as  np
import time
import json
import grovepi
import RPi.GPIO as gpio
import serial

class LightKalman:

    def __init__(self):
        self.f = KalmanFilter (dim_x=2, dim_z=1)
        self.pre = 2
        self.f.x = np.array([self.pre, 7]) #Position and velocity
        self.f.F = np.array([[1.,1.],  [0.,1.]])#Transition matrix
        self.f.H = np.array([[1.,0.]])#Measurement function
        self.f.P = np.array([[1000.,    0.], [   0., 1000.] ]) #covariance  matrix
        self.f.R = np.array([[1.3]]) #Measurement noise
        self.f.Q = Q_discrete_white_noise(dim=2, dt=0.1, var=0.13) #process noise

    def predict(self):
	a = self.f.get_prediction()
	a = a[(0)]
        return float(a[0])

    def update(self, sensor_value):
        a = self.f.get_prediction()
        a = a[(0)]
        print("kalman - " + str(a[0]))
        z = sensor_value
        l = z/(1023.0)
        print("Process  - " + str(l) + "   original - " +  str(z))
        self.f.update(z)
