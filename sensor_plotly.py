import time
import PlotlyController
import SensorController

pc = PlotlyController()
sc = SensorController()

    try:
        pc.startStream()

        while True:

            sound_value = sc.readSound()
            motion_value = sc.readMotion()
            light_value = sc.readLight()
            [temp_value,humid_value] = sc.readTemp_Humid()
            time_value = time.strftime('%H:%M:%S')

            pc.plotGraph(sound_value,light_value,time_value)
            time.sleep(0.1)
            
    except KeyboardInterrupt
        pc.stopStream()




          
            

            
