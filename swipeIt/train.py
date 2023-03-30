import requests, urllib.request # for communication
import time                     # for sleep
import pandas as pd             # for reading data
import numpy as np              # for calculations
import cv2                      # for image viewing
from scipy.stats import kurtosis, skew
from sklearn import svm

IPAddress = '192.168.1.10:8080'  #IP address and port This is different for each person and specified by the phyphox app

start_dat = 'http://' + IPAddress + '/control?cmd=start'  #Starting a data collection
clear_dat = 'http://' + IPAddress + '/control?cmd=clear'  #Clearing a data collection
stop_dat = 'http://' + IPAddress + '/control?cmd=stop'    #Starting a data collection
save_dat = 'http://' + IPAddress + '/export?format=0'     #Saving data

data_dur = 2           # amount of time to collect data
delay    = 0.1         # sleep time


def getData():
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

    return data



def getFeatures(df):
    if df is None:
        return

    x = df['Linear Acceleration x (m/s^2)'].to_numpy()
    y = df['Linear Acceleration y (m/s^2)'].to_numpy()
    z = df['Linear Acceleration z (m/s^2)'].to_numpy()

    # mean
    xmean = x.mean()
    ymean = y.mean()
    zmean = z.mean()

    # standard deviation
    xstd = x.std()
    ystd = y.std()
    zstd = z.std()

    # median
    xmedian = np.median(x)
    ymedian = np.median(y)
    zmedian = np.median(z)

    # skewness
    xs = skew(x)
    ys = skew(y)
    zs = skew(z)

    # kurtosis
    xk = kurtosis(x)
    yk = kurtosis(y)
    zk = kurtosis(z)

    # energy
    xe = np.sum(x**2)/100
    ye = np.sum(y**2)/100
    ze = np.sum(z**2)/100


    # FFT
    xfft = np.fft.fft(x)
    yfft = np.fft.fft(y)
    zfft = np.fft.fft(z)

    return [xmean,ymean,zmean,xstd,ystd,zstd,xmedian,ymedian,zmedian,xs,ys,zs,xk,yk,zk,xe,ye,ze,xfft,yfft,zfft]





def collectData():
    # empty dataframe
    df = pd.DataFrame()

    # collect 20 sample data
    for i in range(5):
        print('Collecting data: ',i)
        data = getData()
        features = getFeatures(data)
        df.loc[len(df)] = features
        print('Pausing for 2s')
        time.sleep(2)

    df.to_csv('data.csv')


def modelTraining(X,y)
    clf = svm.SVC(kernel='linear', C=1.0)
    clf.fit(X,y)


def predict(newData):
    print(clf.predict([newData]))