import os
import sys
import numpy as np
import pandas as pd

#Include your library path in sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

#Include your Library
from graph_library.pltgraph import Plot
from graph_library.csvreader import csv_data

#save_path = save figure
#data_path = csv file path
save_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'figure')
data_path_1 = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data\\exp1\\2N3906\\2000.11.12.exp_3-1-2_1kOhm_I_E_V_BE_pnp.csv')

#data = dictionary format data from WaveForms exported raw data
data = csv_data(data_path_1)
X_6 = -data['V2']
Y_6 = -data['V1']/1000

data_path_2 = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data\\exp1\\2N3904\\2000.11.12.exp_3-1-2_1kOhm_I_E_V_BE.csv')

#data = dictionary format data from WaveForms exported raw data
data = csv_data(data_path_2)
X_4 = data['V2']
Y_4 = data['V1']/1000
Plot([X_4, X_6], [Y_4, Y_6] , X_unit = 'V', Y_unit = 'A', X_name = '$V_{BE}$', Y_name = '$I_{E}$', graph_name = 'both_I_E_V_BE', save_path = save_path, linear_fit = False, File_format = 'jpg', labels = ['2N3904', '2N3906'])
