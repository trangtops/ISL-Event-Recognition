import plotly.plotly as plotly
import plotly.tools as tools
import plotly.graph_objs as go
import time

class PlotlyController:

    def __init__(self):
        self.username = 'trangtops'
        self.apikey = 'csRULP61Y5yZ8qYVjTN9'
        self.light_token = 'pajbficbtq'
        self.sound_token = 'xnqm2wcrgx'
        plotly.sign_in(self.username,self.apikey)

        self.sound_stream = plotly.Stream(self.sound_token)
        self.light_stream = plotly.Stream(self.light_token)
        
    
    def createGraph(self):
        sound_trace = go.Scatter(
         x=[],y=[],
        stream=dict(token=self.light_token,maxpoints=100))
        light_trace = go.Scatter(
        x=[],y=[],
        stream=dict(token=self.sound_token, maxpoints=100),xaxis='x2',yaxis='y2')

        layout = go.Layout(title='ISL Sensor Data')

        figures = tools.make_subplots(rows=2,cols=2)
        figures.append_trace(sound_trace, 1,1)
        figures.append_trace(light_trace,1,2)
        print(plotly.plot(figures, filename='ISL Sensor Data'))

    def startStream(self):
        self.sound_stream.open()
        self.light_stream.open()

    def plotGraph(self,sound_value,light_value,time_value):
        self.sound_stream.write({'x': time_value,'y':sound_value})
        self.light_stream.write({'x': time_value,'y':light_value})

    def stopStream(self):
        self.sound_stream.close()
        self.light_stream.close()
