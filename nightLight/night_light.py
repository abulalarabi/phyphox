import requests, urllib.request # for communication
import time                     # for sleep
import pandas as pd             # for reading data
import numpy as np              # for calculations
import cv2                      # for image viewing

IPAddress = '10.228.21.56:8080'  #IP address and port This is different for each person and specified by the phyphox app

start_dat = 'http://' + IPAddress + '/control?cmd=start'  #Starting a data collection
clear_dat = 'http://' + IPAddress + '/control?cmd=clear'  #Clearing a data collection
stop_dat = 'http://' + IPAddress + '/control?cmd=stop'    #Starting a data collection
save_dat = 'http://' + IPAddress + '/export?format=0'     #Saving data

data_dur = 1           # amount of time to collect data
delay    = 0.1         # sleep time

# read two images
lightOn  = cv2.imread("../../raster/lightson.png")
lightOff = cv2.imread("../../raster/lightsoff.png")

while True:                                           # Continue forever

    # start sensor record
    try:
        print('Poking device to capture data')
        urllib.request.urlopen(clear_dat)             # Clear previous data
        urllib.request.urlopen(start_dat)             # Start collecting data!!
        
    except:
        print('Device Failed to Start')
            
    time.sleep(data_dur)                              # let the device to collect some data
    
    # get data
    try:
        urllib.request.urlopen(stop_dat)              # Stop data collection
        r = requests.get(save_dat)                    # Get data (in excel file)
        open('./data.xls', 'wb').write(r.content)     # Save data for later use
    except:
        print('Device Failed to Collect Data')

    # calculate average of the readings
    data = pd.read_excel('./data.xls')                # Read the saved data
    lux = np.mean(data['Illuminance (lx)'].to_list())
    print('Mean lux: ', lux,'\n')


    # controling interface
    if lux<15:                                        # set this to desired value
        cv2.imshow('Light Status', lightOff)
    else:
        cv2.imshow('Light Status', lightOn)


    # if q button is pressed then exit
    if cv2.waitKey(int(delay*1000)) & 0xFF == ord('q'):
        urllib.request.urlopen(clear_dat)             # Clear previous data
        urllib.request.urlopen(stop_dat)              # Stop data collection
        exit()                                        # exit the program