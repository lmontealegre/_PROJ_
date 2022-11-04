from time import sleep
import piplates.DAQCplate as DAQC
port = 0
for port in range(0,7):
    DAQC.setDOUTbit(0,port)
    sleep(.1)
port = 0
for port in range(0,7):
    DAQC.clrDOUTbit(0,port)
    sleep(.3)
