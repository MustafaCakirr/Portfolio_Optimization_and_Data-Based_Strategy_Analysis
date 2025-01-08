import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from File_Operations_and_Preprocessing import * 


"""Birden fazla şirketin günlük kapanış verilerini tarih ekseninde karşılaştırmalı olarak görselleştirme işlemi."""

def comp_data(*firm_data_list):                                     # Birden fazla argüman alıp bunları bir tupple içinde işleyen fonksiyon
    colors = ['blue','red','green','orange','brown','pink']         # Firmaların grafik üzerindeki renkleri  
    colors_index = 0                                                # Renk listesinin farklı firmalarda farklı renkler kullanılmak için indekslenmesi.
  
    for firm in firm_data_list:                                     # Argüman olarak girilen firmaların sırası ile döngüye sokulması.
        firm['Tarih'] = pd.to_datetime(firm['Tarih'], format='%d-%m-%Y')    # Firma tarih verilerinin pandas datetime formatına sokulaması.
        firm.set_index('Tarih', inplace=True)
        company_close = firm['Kapanış(TL)']
        firm_name = [k for k, v in globals().items() if v is firm][0]       # Firmaların isimlerinin global değişkenler arasında isimlerinin bulunması ve grafikte etiket olarak kullanılması
        plt.plot(company_close, label=f"{firm_name}", color = colors[colors_index])
        plt.title('İki Şirketin Kapanış Fiyatlarının Karşılaştırılması')
        plt.xlabel('Tarih')
        plt.ylabel('Kapanış Fiyatı (TL)')
        plt.legend()
        plt.grid(True)
        colors_index += 1                                             # Yeni firma için renk listesinin bir sonraki indeksinden farklı renk kodunun çağırılması.

    plt.show()
