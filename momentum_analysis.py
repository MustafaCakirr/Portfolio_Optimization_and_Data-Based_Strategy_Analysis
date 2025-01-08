import pandas as pd
import numpy as np 
from File_Operations_and_Preprocessing import * 

""" İstenilen gün aralığında hisselerin kapanış fiyatının hesaplanması. """

def momentum(firm,comp_day):            # Firma ve Karşılaştırılacak gün sayısının argüman olarak girilmesi.
    momentum_period = comp_day 
    firm_momentum = firm['Kapanış(TL)'].pct_change(periods=momentum_period)  # Belirlenen gün aralığında fiyat değişiminin hesaplanmas.
    return print(firm_momentum)  # Son dönemin momentumunu gör
