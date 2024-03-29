import requests, urllib.request # for communication
import time                     # for sleep
import pandas as pd             # for reading data
import numpy as np              # for calculations
import cv2                      # for image viewing

# change this to true if you are using audio
IS_SOUND = False
IPAddress = 'xxx.xxx.xxx.xxx:8080'  #IP address and port This is different for each person and specified by the phyphox app

start_dat = 'http://' + IPAddress + '/control?cmd=start'  #Starting a data collection
clear_dat = 'http://' + IPAddress + '/control?cmd=clear'  #Clearing a data collection
stop_dat = 'http://' + IPAddress + '/control?cmd=stop'    #Starting a data collection
save_dat = 'http://' + IPAddress + '/export?format=0'     #Saving data

data_dur = 1           # amount of time to collect data
delay    = 0.1         # sleep time

# read two images
# IF YOU ARE USING SOUND, you can use soundon.png and soundoff.png files.
lightOn  = cv2.imread("./rasters/lightson.png")         # raster to show when lights on
#soundOn = cv2.imread("./rasters/soundon.png")

# Load raster to show when lights off
# ***** YOUR CODE ***** #




while True:                                           # Continue forever

    # start sensor record
    try:
        print('Poking device to capture data')
        urllib.request.urlopen(clear_dat)             # Clear previous data
        
        # Now Start collecting data in a similar way using start_dat
        # ***** YOUR CODE ***** #


        
    except:
        print('Device Failed to Start\nCheck the IP address and if the App is running')
            
    time.sleep(data_dur)                              # let the device to collect some data
    
    # get and save data
    try:
        # Now stop collecting data in a similar way using stop_dat
        # ***** YOUR CODE ***** #


        
        r = requests.get(save_dat)                    # Get data (in excel file)
        open('./data.xls', 'wb').write(r.content)     # Save data for later use
    except:
        print('Device Failed to Collect Data')

    
    # read the captured data
    data = pd.read_excel('./data.xls')                # Read the saved data
    # Change this one to the particular column name
    if IS_SOUND == False:
        rawData = data['Illuminance (lx)'].to_list()
    else:
        rawData = data['Sound pressure level (dB)'].to_list()[3:-1]
    

    # sound or illuminance is a list of data that contains the audio or lux value
    # now calculate mean value of the illumincance or sound value
    # NOTE: the variable name here is meanValue
    # ***** YOUR CODE ***** #



    # print the mean value of illuminance or sound
    # then take note with and without putting your hands over the smartphone
    # if you are using audio then take note with and without sound
    # ***** YOUR CODE ***** #



    # Set a threshold value
    # this value can be the average of two readings that you noted before
    # ***** YOUR CODE ***** #
    threshold = 0                                   # set this to desired value



    # controling interface
    if meanValue<threshold:
        # show the lightOff/soundOff raster in the window named 'Light Status' or 'Sound Status'
        # example: cv2.imshow('Light Status', lightOff)
        # ***** YOUR CODE ***** #
        
    else:
        # show the lightOn/soundOn raster in the window named 'Light Status' or 'Sound Status'
        # ***** YOUR CODE ***** #



    # if q button is pressed then exit
    if cv2.waitKey(int(delay*1000)) & 0xFF == ord('q'):
        # Clear data collection
        # ***** YOUR CODE ***** #
        
        
        # Stop data collection
        # ***** YOUR CODE ***** #


        exit()                                        # exit the program
