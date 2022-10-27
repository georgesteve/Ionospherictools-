#This algorithm it's an adaptation to  Liam M. Kilcommons code https://github.com/lkilcommons/nasaomnireader/blob/master/nasaomnireader/omnireader.py
#It asks for the date and return the variables needed to make a prediction with the machine learning model developed.
#DEveloped in python3

def download_omni_text_modelo(input_datetime):
    #Create a time window
    sTimeIMF = input_datetime
    eTimeIMF = input_datetime+ datetime.timedelta(1) 

    #omni_interval is a dictionary-like object
    #that you can use to get the omni data for
    #any variable as a numpy array
    #for any span of time
    omniInt = omnireader.omni_interval(sTimeIMF-datetime.timedelta(1),eTimeIMF+datetime.timedelta(1),'5min')
    t = omniInt['Epoch'] #datetime timestamps
    #By,Bz = omniInt['BY_GSM'],omniInt['BZ_GSM']

    IMF,By,Bz,Bx,AE,proton_density= omniInt['IMF'], omniInt['BY_GSM'],omniInt['BZ_GSM'],omniInt['BX_GSE'],omniInt['AE_INDEX'], omniInt['proton_density']
    vsw,psw = omniInt['flow_speed'], omniInt['Pressure']


    omniInt_1hr = omnireader.omni_interval(sTimeIMF-datetime.timedelta(1),eTimeIMF+datetime.timedelta(1),'hourly', cdf_or_txt = 'txt')
    epochs_1hr = omniInt_1hr['Epoch'] #datetime timestamps
    F107,KP,DST = omniInt_1hr['F10_INDEX'],omniInt_1hr['KP'],omniInt_1hr['DST']

    #resample OMNI Solar Wind Data
    
    IMF_data = pd.Series(IMF, index = t).resample('1T').pad().truncate(sTimeIMF, eTimeIMF)
    By_data = pd.Series(By, index = t).resample('1T').pad().truncate(sTimeIMF, eTimeIMF)
    Bz_data = pd.Series(Bz, index = t).resample('1T').pad().truncate(sTimeIMF, eTimeIMF)
    Bx_data = pd.Series(Bx, index = t).resample('1T').pad().truncate(sTimeIMF, eTimeIMF)
    proton_density_data = pd.Series(proton_density, index = t).resample('1T').pad().truncate(sTimeIMF, eTimeIMF)
    AE_data = pd.Series(AE, index = t).resample('1T').pad().truncate(sTimeIMF, eTimeIMF)
    
    F107data = pd.Series(F107, index = epochs_1hr).resample('1T').pad().truncate(sTimeIMF, eTimeIMF)
    KPdata = pd.Series(KP, index = epochs_1hr).resample('1T').pad().truncate(sTimeIMF, eTimeIMF)
    DST_data = pd.Series(DST, index = epochs_1hr).resample('1T').pad().truncate(sTimeIMF, eTimeIMF)
    


    #function to find data at previous time intervals
    def roll_back(data, minutes = 1):
        ts = sTimeIMF - datetime.timedelta(minutes = minutes)
        te = eTimeIMF - datetime.timedelta(minutes = minutes)
        data = pd.Series(data, index = t).resample('1T').pad()
        new_data = data.truncate(ts, te)
        rolled_data = pd.Series(np.array(new_data), index = By_data.index)
        return rolled_data

	#put all in a dataframe and save

    dataframe = pd.DataFrame()
    dataframe['Vector_B'] = IMF_data
    dataframe['BZ'] = Bz_data
   
    
    dataframe['BY'] = By_data
    dataframe['BX'] = Bx_data
    dataframe['SW_Proton']= proton_density_data
    
    dataframe['AE-index'] = AE_data
    dataframe['Dst-index '] = DST_data



    dataframe['Kp_index'] = KPdata
    dataframe['f10.7_index'] = F107data

    #Vector_B 	BX 	BY 	BZ 	SW_Proton 	Kp_index 	R 	Dst-index 	f10.7_index 	AE-index


    return dataframe
    
#from nasaomnireader import omnireader
#import datetime
#import matplotlib.pyplot as plt
#import pandas as pd
#import numpy as np
#a=download_omni_text_modelo(datetime.datetime(2015,1,1))
#print(a)   
