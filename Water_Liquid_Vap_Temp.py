import pandas as pd
import numpy as np

#operate on the assumption that use temp value to get the rest of the properties
#assume user has already verified that P and T values are at or above saturation
class Water_Liquid_vap_Temp(object):
    def __init__(self, filename):
        self.data = pd.read_csv(filename)

    def get_properties(self, T):
        temps = self.data['T']

        #change == later since dtype is float
        lbound = None
        hbound = None
        for i in range(len(temps)):
            if temps[i] == T:
                return self.data.iloc[i] # returns column 
            elif temps[i] < T:
                lbound = i
            elif temps[i] > T:
                hbound = i
        if lbound != hbound:
            return self.lerp(lbound, hbound)
        

    def lerp(self, i1, i2):
        df = {''} # need to interpolate and return df with computed values
        lrow = self.data.iloc[i1]
        hrow = self.data.iloc[i2]
        for l, h in zip(lrow, hrow):

