from re import I
import pandas as pd
from icecream import ic

class Water_Liquid_Vap(object):
    def __init__(self, filename, input_type='None'):
        self.data = pd.read_csv(filename)
        if input_type == 'None':
            self.get_type(filename)
        else:
            try:
                self.verify_input_type(input_type)
            except Exception as e:
                raise e
        # need to check input_type again ( either T or P)
        self.inputs = self.data[self.input_type]
        self.MIN = self.inputs.iat[0]
        self.MAX = self.inputs.iat[-1]

    # Tries to determine if it is using T table or P table and setting input_type accordingly
    def get_type(self, filename):
        if filename.upper().find('TEMP') > -1:
            self.input_type = 'T'
        elif filename.upper().find('PRES') > -1:
            self.input_type = 'P'
    
    def verify_input_type(self, input_type):
        try:
            input_type = input_type.strip().upper()
            if input_type == 'T' or input_type == 'P':
                self.input_type = input_type
            else:
                raise Exception('type exception')
        except Exception as e:
            raise e


    def get_properties(self, input):
    
        #change == later since dtype is float
        # check if T < MaxT and T > minT

        if input < self.MIN or input > self.MAX:
            ic(self.input_type + ' out of range')
            return None

        lbound = None
        hbound = None
        for i in range(len(self.inputs)):
            if self.inputs[i] == input:
                ic('Found')
                return self.data.iloc[i] # returns column 
            elif self.inputs[i] < input:
                lbound = i
            elif self.inputs[i] > input:
                hbound = i
                break #finding l and h bounds
        if lbound < hbound:
            ic('interp')
            ic(lbound)
            ic(hbound)
            return self.interpolate(lbound, hbound, input)
            
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