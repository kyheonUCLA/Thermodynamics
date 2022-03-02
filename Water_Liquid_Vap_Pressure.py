import pandas as pd
from icecream import ic

class Water_Liquid_Vap_Pressure(object):
    def __init__(self, filename):
        self.data = pd.read_csv(filename)
        self.MIN_P = self.data['P'].iat[0]
        self.MAX_P = self.data['P'].iat[-1]
    
    def get_properties(self, P):
        pressures = self.data['P']
        if P < self.MIN_P or P > self.MAX_P:
            ic('P out of range')
            return None
        
        lbound = None
        hbound = None
        for i in range(len(pressures)):
            if pressures[i] == P:
                ic('Found')
                return self.data.iloc[i] # returns column 
            elif pressures[i] < P:
                lbound = i
            elif pressures[i] > P:
                hbound = i
                break #finding l and h bounds
        if lbound < hbound:
            ic('interp')
            ic(lbound)
            ic(hbound)
            return self.interpolate(lbound, hbound, P)


    def interpolate(self, i1, i2, x):  
        lrow = self.data.iloc[i1]
        hrow = self.data.iloc[i2]
        P1 = lrow['P']
        P2 = hrow['P']
        df = lrow.copy(deep=True)
        lerp = lambda p1, p2, x : (p1[1]-p2[1]) / (p1[0]-p2[0]) * (x - p1[0]) + p1[1]
        for key, value in df.iteritems():
            if key == 'P':
                df = df.replace({df[key] : x})
            else:
                y = lerp((P1, lrow[key]), (P2, hrow[key]), x)
                df = df.replace({df[key] : y})
        return df

    #Alexi Guzzman

