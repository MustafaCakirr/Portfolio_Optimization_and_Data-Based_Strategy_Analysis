from telnetlib import PRAGMA_HEARTBEAT
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dataframe_settings import *
from File_Operations_and_Preprocessing import *
import momentum_analysis
from trading_strategy import * 
from graph_data import * 
from momentum_analysis import * 

# momentum(gar_data,100)
# graph_data(gar_data)
momentum(ak_data,1000)