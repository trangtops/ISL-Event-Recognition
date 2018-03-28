import plotly.plotly as plotly
import plotly.tools as tools
import plotly.graph_objs as go
import time

class PlotlyController:

    def __init__(self):
        self.username = 'trangtops'
        self.apikey = 'G4aSatxcvs2P9Up5qruj'
        self.light_token = 'pajbficbtq'
        self.sound_token = 'xnqm2wcrgx'
        plotly.sign_in(username,apikey)

        self.sound_stream = plotly.Stream(sound_token)
        self.light_stream = plotly.Stream(light_token)
        
    
    def createGraph():
        sound_trace = go.Scatter(
         x=[],y=[],
        stream=dict(token=streamtoken1,maxpoints=100))
        light_trace = go.Scatter(
        x=[],y=[],
        stream=dict(token=streamtoken2, maxpoints=100),xaxis='x2',yaxis='y2')

        layout = go.Layout(title='ISL Sensor Data')

        figures = tools.make_subplots(row=2,col=2)
        figures.append_trace(sound_trace, 1,1)
        figures.append_trace(light_trace,1,2)
        print(plotly.plot(fig, filename='ISL Sensor Data'))

    def startStream():
        sound_stream.open()
        light_stream.open()

    def plotGraph(self,sound_value,light_value,time_value):
        sound_stream.write('x': time_value,'y':sound_value)
        light_stream.write('x': time_value,'y':light_value)

    def stopStream():
        sound_stream.close()
        light_stream.close()
