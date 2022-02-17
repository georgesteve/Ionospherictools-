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
    def __init__(self):
        date = date.today() 
        self.d1  = date - timedelta(days = int(date.strftime("%d"))-1)
        self.d2 = date.replace(day = calendar.monthrange(date.year, date.month)[1])

    def muestra(self):
        return self.d1 , self.d2

limite = S4()
print("Área del rectángulo: ", limite.muestra())
