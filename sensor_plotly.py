from PlotlyController import PlotlyController
#import SensorController
import random
import time 

pc = PlotlyController()
#sc = SensorController()

try:
    pc.createGraph()
    pc.startStream()

    while True:

        #sound_value = sc.readSound()
        #motion_value = sc.readMotion()
        #light_value = sc.readLight()
        #[temp_value,humid_value] = sc.readTemp_Humid()
        time_value = time.strftime('%H:%M:%S')
        sound_value = random.randint(0,10)
        light_value = random.randint(1,3)
            
        pc.plotGraph(sound_value,light_value,time_value)
        time.sleep(0.1)

except KeyboardInterrupt:
    pc.stopStream()

#except ConnectionAbortedError:

