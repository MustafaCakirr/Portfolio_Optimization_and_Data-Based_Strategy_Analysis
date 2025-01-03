import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from turtle import color
from file_operations_and_preprocessing import * 

pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)  # Veri çerçevesini satırlara bölme

def graph_data(firm_data):
    firm_data['Tarih'] = pd.to_datetime(firm_data['Tarih'], format='%d-%m-%Y')
    firm_data.set_index('Tarih', inplace=True)
    
    # Eksik verileri kontrol et
    print("Eksik Veri Kontrolü:\n", firm_data.isnull().sum())
    
    # Eksik verileri doldur (örneğin, ileri doldurma yöntemiyle)
    firm_data.fillna(method='ffill', inplace=True)
    
    # Temel istatistikler
    print("\nTemel İstatistikler:\n", firm_data.describe())
    
    # Fiyatların zaman içindeki değişimi (Kapanış fiyatı)
    plt.figure(figsize=(10, 6))
    firm_data['Kapanış(TL)'].plot(title="Kapanış Fiyatı (TL)")
    plt.xlabel("Tarih")
    plt.ylabel("Fiyat (TL)")
    plt.grid()
    plt.show()
    
    # Korelasyon matrisi ve ısı haritası
    corr_matrix = firm_data.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Korelasyon Matrisi")
    plt.show()

"""def comp_data(firm_data_1,firm_data_2):
    firm_data_1['Tarih'] = pd.to_datetime(firm_data_1['Tarih'], format='%d-%m-%Y')
    firm_data_1.set_index('Tarih', inplace=True)
    
    # Şirket 2'nin verilerini yükle
    firm_data_2['Tarih'] = pd.to_datetime(firm_data_2['Tarih'], format='%d-%m-%Y')
    firm_data_2.set_index('Tarih', inplace=True)
    
    # Her iki şirketin "Kapanış (TL)" fiyatlarını al
    company_close_1 = firm_data_1['Kapanış(TL)']
    company_close_2 = firm_data_2['Kapanış(TL)']
    
    # Grafik üzerinde her iki şirketin fiyatlarını karşılaştır
    plt.figure(figsize=(12, 6))

    # Şirket 1'in kapanış fiyatını çiz
    plt.plot(company_close_1, label="Şirket 1 Kapanış (TL)", color='blue')
    
    # Şirket 2'nin kapanış fiyatını çiz
    plt.plot(company_close_2, label="Şirket 2 Kapanış (TL)", color='red')
    
    # Grafik başlığı ve etiketler
    plt.title('İki Şirketin Kapanış Fiyatlarının Karşılaştırılması')
    plt.xlabel('Tarih')
    plt.ylabel('Kapanış Fiyatı (TL)')
    plt.legend()
    
    # Grafik gösterimi
    plt.grid(True)
    plt.show()"""

def comp_data(*firm_data_list):
    colors = ['blue','red','green','orange','brown','pink']
    colors_index = 0 
   

    for firm in firm_data_list:
        firm['Tarih'] = pd.to_datetime(firm['Tarih'], format='%d-%m-%Y')
        firm.set_index('Tarih', inplace=True)
        company_close = firm['Kapanış(TL)']
        firm_name = [k for k, v in globals().items() if v is firm][0]
        plt.plot(company_close, label=f"{firm_name}", color = colors[colors_index])
        plt.title('İki Şirketin Kapanış Fiyatlarının Karşılaştırılması')
        plt.xlabel('Tarih')
        plt.ylabel('Kapanış Fiyatı (TL)')
        plt.legend()
        plt.grid(True)
        colors_index += 1

        
    plt.show()

def cov_matrix():
    asel_return =   asel_data['Kapanış(TL)'].pct_change().dropna()
    thy_return =    thy_data['Kapanış(TL)'].pct_change().dropna()
    tupr_return =   tupr_data['Kapanış(TL)'].pct_change().dropna()
    gar_return =    gar_data['Kapanış(TL)'].pct_change().dropna()
    koc_return =    koc_data['Kapanış(TL)'].pct_change().dropna()
    ford_return =   ford_data['Kapanış(TL)'].pct_change().dropna()
    ak_return =     ak_data['Kapanış(TL)'].pct_change().dropna()
    
    returns_data = pd.DataFrame({
    'Aselsan': asel_return,
    'THY': thy_return,
    'Tupras': tupr_return,
    'Garanti': gar_return,
    'Koc': koc_return,
    'Ford': ford_return,
    'Akbank': ak_return
    })
  
    return print(returns_data.cov())

def momentum(firm,comp_day):
    momentum_period = comp_day # x günlük momentum analizi
    firm_momentum = firm['Kapanış(TL)'].pct_change(periods=momentum_period)  # Yüzde değişimi hesapla
    return print(firm_momentum.tail(100))  # Son dönemin momentumunu gör
  
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
    