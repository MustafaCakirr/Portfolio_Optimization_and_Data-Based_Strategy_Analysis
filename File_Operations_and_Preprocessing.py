import pandas as pd
import numpy as np 

"""DOSYA İŞLEMLERİ"""
asel_data   = pd.read_excel("D:/bist_hisseler/aselsan_hisse.xlsx")
ak_data     = pd.read_excel("D:/bist_hisseler/akbankhisse.xlsx")
ford_data   = pd.read_excel("D:/bist_hisseler/fordhisse.xlsx")
gar_data    = pd.read_excel("D:/bist_hisseler/garantihisse.xlsx")
koc_data    = pd.read_excel("D:/bist_hisseler/kochisse.xlsx")
thy_data    = pd.read_excel("D:/bist_hisseler/thyhisse.xlsx")
tupr_data   = pd.read_excel("D:/bist_hisseler/tuprashisse.xlsx")

"""VERİ ÇIKARMA İŞLEMLERİ"""
asel_data   = asel_data.drop(['Sermaye(mn TL)'],axis = 1)
ak_data     = ak_data.drop(['Sermaye(mn TL)'],axis = 1)
ford_data   = ford_data.drop(['Sermaye(mn TL)'],axis = 1)
gar_data    = gar_data.drop(['Sermaye(mn TL)'],axis = 1)
koc_data    = koc_data.drop(['Sermaye(mn TL)'],axis = 1)
thy_data    = thy_data.drop(['Sermaye(mn TL)'],axis = 1)
tupr_data   = tupr_data.drop(['Sermaye(mn TL)'],axis = 1)


""" VERİ GÖRÜNTÜLEME """
def firm_info(firm):
    print(firm.to_string())

def asel_info():
    print(asel_data.to_string())

def ak_info():
    print(ak_data.to_string()) 

def ford_info():
    print(ford_data.to_string())

def koc_info():
    print(koc_data.to_string())

def thy_info():
    print(thy_data.to_string())

def tupr_info():
    print(tupr_data.to_string())

def gar_info():
    print(gar_data.to_string())

