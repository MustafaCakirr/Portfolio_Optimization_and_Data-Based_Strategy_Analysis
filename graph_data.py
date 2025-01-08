import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from File_Operations_and_Preprocessing import * 
import seaborn as sns

def graph_data(firm_data):
    firm_data['Tarih'] = pd.to_datetime(firm_data['Tarih'], format='%d-%m-%Y')  # Firma tarih verilerinin pandas datetime formatına sokulaması.
    firm_data.set_index('Tarih', inplace=True)
    
   
    print("Eksik Veri Kontrolü:\n", firm_data.isnull().sum())                   # Eksik verilerin kontrol edilmesi. Hangi veride kaç eksik var bulunması.
    
    
    firm_data.fillna(method='ffill', inplace=True)                              # Eksik verilerin doldurulması.
    
    
    print("\nTemel İstatistikler:\n", firm_data.describe())                     # Firmanın temel istatistiklerinin hesaplanması.
    
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
