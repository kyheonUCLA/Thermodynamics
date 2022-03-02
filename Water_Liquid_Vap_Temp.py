import pandas as pd
import numpy as np

class Water_Liquid_vap_Temp(object):
    def __init__(self, filename):
        self.col_header = ['Temp', 'Pressure', 'vf', 'vg', 'uf', 'ug', 'hf', 'hfg', 'hg', 'sf', 'sfg', 'sg']
        self.data = df.read_csv(filename)

