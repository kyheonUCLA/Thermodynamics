import pandas as pd
from icecream import ic
#operate on the assumption that use temp value to get the rest of the properties
#assume user has already verified that P and T values are at or above saturation

#might be able to abstract this to also include pressure table
class Water_Liquid_Vap_Temp(object):
    def __init__(self, filename):
        self.data = pd.read_csv(filename)
        self.MIN_T = self.data['T'].iat[0]
        self.MAX_T = self.data['T'].iat[-1]

    def get_properties(self, T):
        temps = self.data['T']
        #change == later since dtype is float
        # check if T < MaxT and T > minT

        if T < self.MIN_T or T > self.MAX_T:
            ic('T out of range')
            return None

        lbound = None
        hbound = None
        for i in range(len(temps)):
            if temps[i] == T:
                ic('Found')
                return self.data.iloc[i] # returns column 
            elif temps[i] < T:
                lbound = i
            elif temps[i] > T:
                hbound = i
                break #finding l and h bounds
        if lbound < hbound:
            ic('interp')
            ic(lbound)
            ic(hbound)
            return self.interpolate(lbound, hbound, T)
            
        ic('Other')
        

    def interpolate(self, i1, i2, x):  
        lrow = self.data.iloc[i1]
        hrow = self.data.iloc[i2]
        T1 = lrow['T']
        T2 = hrow['T']
        df = lrow.copy(deep=True)
        lerp = lambda p1, p2, x : (p1[1]-p2[1]) / (p1[0]-p2[0]) * (x - p1[0]) + p1[1]
        for key, value in df.iteritems():
            if key == 'T':
                df = df.replace({df[key] : x})
            else:
                y = lerp((T1, lrow[key]), (T2, hrow[key]), x)
                df = df.replace({df[key] : y})
        return df

