import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from turtle import color
from File_Operations_and_Preprocessing import * 



def mov_avg(firm,min_time,max_time): # Moving Avarage
    # Kısa ve uzun dönemli hareketli ortalamalar
    short_window = min_time
    long_window = max_time
    
    # Kısa dönemli hareketli ortalama (SHORT SMA)
    firm['SHORT SMA'] = firm['Kapanış(TL)'].rolling(window=short_window, min_periods=1).mean()
    
    # Uzun dönemli hareketli ortalama (LONG SMA)
    firm['LONG SMA'] = firm['Kapanış(TL)'].rolling(window=long_window, min_periods=1).mean()
    
    # Momentum sinyali (kısa dönem SMA uzun dönem SMA'yı yukarı doğru geçtiğinde alım sinyali)
    firm['Momentum_Signal'] = 0
    firm['Momentum_Signal'][short_window:] = np.where(firm['SHORT SMA'][short_window:] > firm['LONG SMA'][short_window:], 1, 0)
    
    # Grafik ile gösterim
    plt.figure(figsize=(10,6))
    plt.plot(firm['Kapanış(TL)'], label="Şirket Kapanış Fiyatı")
    plt.plot(firm['SHORT SMA'], label=f"{short_window}-gün SMA", color='orange')
    plt.plot(firm['LONG SMA'], label=f"{long_window}-gün SMA", color='green')
    plt.title("Şirket Momentum Analizi - SMA")
    plt.legend(loc='best')
    plt.show() 