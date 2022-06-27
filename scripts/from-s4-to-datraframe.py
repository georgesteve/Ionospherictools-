# This script contain functions to obtain a .s4 file and to convert it into .csv (dataframe)
#  Format : ['Año','Day','Tiempo','PRN','S4','Az','Elv'])  
# Tiempo: time of the day in seconds (s)
# Elv, Az: sexagesimal degrees (°)
# Author: George Fajardo
# 

import os
import gzip
import shutil
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()
from matplotlib import pyplot as plt
import datetime
import time




def obtaindateliteral(yday,year):

    if(year<10):
        string=str(yday)+","+"0"+str(year)
    else:
        string=str(yday)+","+str(year)
    time_1 = time.strptime(string,"%j,%y")
  #time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    return (time_1.tm_year,time.strftime("%B",time_1),time_1.tm_mon)

    
    
def agregaarchivo(data_file,df_marks):
    S4frame=[]
    # Delimiter
    data_file_delimiter ='\s+'
    
    # The max column count a line in the file could have
    largest_column_count = 0

    # Loop the data lines
    with open(data_file, 'r') as temp_f:
        # Read the lines
        lines = temp_f.readlines()

        for l in lines:
            # Count the column count for the current line
            column_count = len(l.split())+ 1
            df=l.split()
            if float(df[0])<2000:
                Año=df[0]                       

                Day=df[1]

                Tiempo=df[2]
                Nsats=df[3]
                Nsats=int(Nsats)
                
                for x in range(0, len(l.split())):
                    if (x-4)%4==0 and ((Nsats+1)*4)> x > 3:
                        Satélite=df[x]

                    if (x-5) % 4==0 and ((Nsats+1)*4)>x>4:
                        #print("S4:",df[x][y])
                        S4=df[x]
                    
                    if (x-6) % 4==0 and ((Nsats+1)*4)>x>5:
                        #print("Az:",df[x][y])
                        Az=df[x]

                    if (x-7) % 4==0 and ((Nsats+1)*4)>x>6:
                        #print("Elv:",df[x][y])
                        Elv=df[x]
                        
                        c=[]
                        c.append(Año)
                        c.append(Day)
                        c.append(Tiempo)
                        c.append(Satélite)
                        c.append(S4)
                        c.append(Az)
                        c.append(Elv)
                        S4frame.append(c)
                        #print(S4frame)
        df = pd.DataFrame(S4frame, columns = ['Año','Day','Tiempo','PRN','S4','Az','Elv'])
        df_marks=pd.concat([df_marks,df])
        print(len(df_marks))


    # Close file
    temp_f.close()

   
    return df_marks

 

def devolverArchivos(carpeta):

    count=0

    for archivo in os.listdir(carpeta):

            count=count+1
            with gzip.open(os.path.join(carpeta,archivo), 'rb') as f_in:
                with open('Downloads\Datos Edgardo1\lji-Summer-08&09 Huancayo.s4', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
 

            # Input
            data_file='Downloads\Datos Edgardo1\lji-Summer-08&09 Huancayo.s4'
        
            if (count<2):
                        #Creating a new dataframe
                df_marks = pd.DataFrame(columns=['Año','Day','Tiempo','PRN','S4','Az','Elv'])        
                listaF=agregaarchivo(data_file,df_marks)
                print(os.path.join(carpeta,archivo))
                print(count)
            else:
                listaF=agregaarchivo(data_file,listaF)
                print(os.path.join(carpeta,archivo))
                print(count)

            if os.path.isdir(os.path.join(carpeta,archivo)):
                devolverArchivos(os.path.join(carpeta,archivo)) #parte recursiva, es decir para leer todas las subcarpetas
    
    return(listaF)          

            
#Mli=devolverArchivos("Downloads/tacjul21")
#devolverArchivos("/home/gfajardo/Desktop/Datos 121001/gfajardo_9sbmuc/")
#print(Mli)
#devolverArchivos("/home/gfajardo/Desktop/Datos 121001/gfajardo_9sbmuc")
#Mli.to_csv(r'Downloads\S4-tacna-julio-2021.csv')
