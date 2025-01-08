import pandas as pd
import numpy as np 
from File_Operations_and_Preprocessing import * 
 
""" Hisse senetlerinin yüzdesel günlük fiyat değişiminin hesaplanması """

def cov_matrix():
    asel_return =   asel_data['Kapanış(TL)'].pct_change().dropna()  # pct_change() metodu ile bir gün önceki fiyatı ile bugünkü fiyatı arasında yüzdesel değişimi bulmaya yarar.
    thy_return =    thy_data['Kapanış(TL)'].pct_change().dropna()   # dropna() metodu ile 1. günün yüzdesel değişim değeri NaN olacağı için NaN değerini düşürür.
    tupr_return =   tupr_data['Kapanış(TL)'].pct_change().dropna()
    gar_return =    gar_data['Kapanış(TL)'].pct_change().dropna()
    koc_return =    koc_data['Kapanış(TL)'].pct_change().dropna()
    ford_return =   ford_data['Kapanış(TL)'].pct_change().dropna()
    ak_return =     ak_data['Kapanış(TL)'].pct_change().dropna()
    
    returns_data = pd.DataFrame({                                   # Elde edilen kovaryans matrisleri DataFrame içerisinde toplanıp ekrana bastırılması.
    'Aselsan': asel_return,
    'THY': thy_return,
    'Tupras': tupr_return,
    'Garanti': gar_return,
    'Koc': koc_return,
    'Ford': ford_return,
    'Akbank': ak_return
    })
  
    return print(returns_data.cov())