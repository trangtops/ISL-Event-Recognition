import time
import json
import grovepi
import RPi.GPIO as gpio
import serial
import plotly.plotly as plotly
import plotly.tools as tools
import plotly.graph_objs as go

# Setup Raspberry Pi
gpio.setmode(gpio.BCM)
gpio.setup(25, gpio.IN)

light_pin = 0
sound_pin = 1
dht_pin = 7

grovepi.pinMode(light_sensor_pin, "INPUT")
grovepi.pinMode(sound_sensor_pin, "INPUT")

s1 = serial.Serial(port, 9600)
s1.flushInput()

# Setup Ploty
username = 'trangtops'
apikey = 'G4aSatxcvs2P9Up5qruj'
light_token = 'pajbficbtq'
sound_token = 'xnqm2wcrgx'
temp_token = 's96vqjowbq'

plotly.sign_in(username,apikey)
sound_trace = go.Scatter(
    x=[],y=[],
    stream=dict(
        token=streamtoken1,
        maxpoints=200
    )
)

light_trace = go.Scatter(
    x=[],y=[],
    stream=dict(
        token=streamtoken2,
        maxpoints=200
    ),
    xaxis='x2',
    yaxis='y2'
)

layout = go.Layout(
    title='ISL Sensor Data'
)

figures = tools.make_subplots(row=2,col=2)
figures.append_trace(sound_trace, 1,1)
figures.append_trace(light_trace,1,2)
print(plotly.plot(fig, filename='Raspberry Pi Streaming Example'))
    try:
        sound_stream = plotly.Stream(sound_token)
        light_stream = plotly.Stream(light_token)
        sound_stream.open()
        light_stream.open()

        while True:
            sound_value = ''
            # read sound value
            for i in range(10):
                sound_value += s1.readline()

            motion_value = gpio.input(25)
            light_value = grovepi.analogRead(light_pin)
            [temp_value,humid_value] = grovepi.dht(dht_pin,0)
            time_value = time.strftime('%H:%M:%S')

            sound_value = sound_value
            sound_stream.write('x': time_value,'y':sound_value)

            
