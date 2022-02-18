#Obtain first day and last day of specific months, by default it is the current day.


import pandas as pd

import pylab as pl
import numpy as np
import matplotlib.pyplot as plt


import matplotlib 
from google.colab import files
import matplotlib.dates as mdates

class S4plots:
    """
    Define un rectángulo según su base y su altura.
    """
    def __init__(self,dataframeS4,dataframeSW):
        
        self.S4  = dataframeS4
        self.SW  = dataframeSW

    def plotS4f107(self,title):

      fig, ax1 = plt.subplots(figsize=(20,6))

      fig.suptitle(title)



      X1 = self.S4['S4']
      Y1 = self.S4.index


      X2 = dataframeSW['Dst-index']
      Y2 = dataframeSW['date_time']
      color = 'tab:olive'



      ax1.tick_params(axis='x',labelsize=14)
      ax1.set_ylabel('S4',fontsize=20)
      # convert the epoch format to matplotlib date format 

      ax1.tick_params(axis='x',labelsize=14)
      ax1.tick_params(axis='y',labelsize=14)
      ax1.set_title("Cintilaciones (Máximo) /Disturbance Storm Time Index-Huancayo",size=18)



      # plot the two cases side by side


      lns1=ax1.plot(Y1,X1, label='S4')

      # pretty up the xaxis labels
      myFmt = mdates.DateFormatter('%m-%d %H')
      ax1.xaxis.set_major_formatter(myFmt)






      ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis




      ax2.set_xlabel('Hora Local', fontsize=20)
      #ax1.set_ylabel('Kpx10', color=color,fontsize=20)
      ax2.set_ylabel('Dst',fontsize=20)

      #ax.hist2d(Y1, X1, (80, 20), cmap=plt.cm.jet)
      lns2=ax2.plot(Y2,X2,color='r', label='Dst')

      ax2.tick_params(axis='x',labelsize=14)
      #ax1.format_xdata = mdates.DateFormatter('%m-%d')
      #ax1.xaxis.set_major_locator(plt.MaxNLocator(8))
      myFmt = mdates.DateFormatter('%m-%d')
      ax2.xaxis.set_major_formatter(myFmt)

      #ax1.set_ylim(0,2)
      #ax1.tick_params(axis='y', labelcolor=color,labelsize=18)
      ax2.tick_params(axis='y',labelsize=14)

      #ax.set_ylim([0, 1])#Rango de valores mostrados entre 0 y 1




      plt.legend()
      plt.show()
    
    def plotS4SF(self,dataframe):
        return dataframe[(dataframe.index > self.d1) & (dataframe.index < self.d2)]
    
    
    
   
limite = Dayfilter()
print("Fechas: ", limite.muestra())
