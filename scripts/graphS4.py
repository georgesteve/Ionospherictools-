import os

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf


from datetime import date, timedelta
import calendar




class S4:
    """
    Define un rectángulo según su base y su altura.
    """
    def __init__(self,today = date.today() ):
        
        self.d1  = today - timedelta(days = int(today.strftime("%d"))-1)
        self.d2  = today.replace(day = calendar.monthrange(today.year, today.month)[1])

    def muestra(self):
        return self.d1 , self.d2

limite = S4()
print("Área del rectángulo: ", limite.muestra())
