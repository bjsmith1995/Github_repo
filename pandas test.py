import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
speedway_dataframe = pd.read_fwf('C:\pythonandsublime\SOP_output.txt')
speedway_dataframe = speedway_dataframe.dropna(axis=0, thresh=6)
bin_to_remove = ['SHOCK', '9999', 'A KIT', 'EMI', 'IVAN']
speedway_dataframe = speedway_dataframe[~speedway_dataframe['BIN'].isin(bin_to_remove)]
print(speedway_dataframe)
print(speedway_dataframe.BIN)