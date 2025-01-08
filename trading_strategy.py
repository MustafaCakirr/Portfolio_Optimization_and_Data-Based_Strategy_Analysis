import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from File_Operations_and_Preprocessing import *

# RSI hesaplama fonksiyonu
def calculate_rsi(data, window):
    delta = data['Kapanış(TL)'].diff()  # Fiyat farklarını al
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()  # Kazançları hesapla
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()  # Kayıpları hesapla
    # RS hesaplama
    rs = gain / loss  
    # Kayıp sıfırsa, RS'yi çok yüksek kabul et ve RSI'yı 100 olarak ayarla
    rs = rs.fillna(0)  # NaN olan RS'leri sıfırla doldur
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_sma(data, window):
    return data['Kapanış(TL)'].rolling(window=window).mean()

def backtest_strategy(data, rsi_window, sma_short, sma_long, initial_balance):
    data['RSI'] = calculate_rsi(data, rsi_window)
    data['SMA_Short'] = calculate_sma(data, sma_short)
    data['SMA_Long'] = calculate_sma(data, sma_long)

    data['Signal'] = 0
    data.loc[(data['RSI'] < 30) & (data['SMA_Short'] > data['SMA_Long']), 'Signal'] = 1  # Al
    data.loc[(data['RSI'] > 70) & (data['SMA_Short'] < data['SMA_Long']), 'Signal'] = -1  # Sat

    balance = initial_balance
    shares = 0
    buy_price = 0

    for i in range(len(data)):
        current_price = data['Kapanış(TL)'].iloc[i]
        signal = data['Signal'].iloc[i]

        # Alım sinyali
        if signal == 1 and balance >= current_price:
            shares += balance // current_price
            balance -= shares * current_price
            buy_price = current_price

        # Satım sinyali
        elif signal == -1 and shares > 0:
            balance += shares * current_price
            shares = 0

    # Son bakiye ve portföy değeri
    final_value = balance + (shares * data['Kapanış(TL)'].iloc[-1])

    print(f"Başlangıç Bakiyesi: {initial_balance} TL")
    print(f"Son Portföy Değeri: {final_value:.2f} TL")
    print(f"Net Kazanç: {final_value - initial_balance:.2f} TL")

    return data

# result= backtest_strategy(asel_data,14,200,1000,1000)

def trade(firm_data):
    backtest_strategy(firm_data,14,200,1000,1000)
    firm_data['Tarih'] = pd.to_datetime(firm_data['Tarih'], format='%d-%m-%Y')
    firm_data.set_index('Tarih', inplace=True)
    plt.figure(figsize=(14, 7))
    plt.plot(firm_data.index, firm_data['Kapanış(TL)'], label='Kapanış Fiyatı', color='blue')
    plt.plot(firm_data.index, firm_data['SMA_Short'], label=f'Short SMA ({300})', color='orange')
    plt.plot(firm_data.index, firm_data['SMA_Long'], label=f'Long SMA ({1800})', color='green')
    plt.scatter(firm_data.index[firm_data['Signal'] == 1], firm_data['Kapanış(TL)'][firm_data['Signal'] == 1], label='Alım Sinyali', marker='^', color='green', alpha=1)
    plt.scatter(firm_data.index[firm_data['Signal'] == -1], firm_data['Kapanış(TL)'][firm_data['Signal'] == -1], label='Satım Sinyali', marker='v', color='red', alpha=1)
    plt.title('RSI ve SMA Tabanlı Strateji Backtest')
    plt.xlabel('Tarih')
    plt.ylabel('Fiyat (TL)')
    plt.legend()
    plt.grid()
    plt.show()