from itertools import tee
from Water_Liquid_Vap_Pressure import Water_Liquid_Vap_Pressure
from Water_Liquid_Vap_Temp import Water_Liquid_Vap_Temp
from Water_Liquid_Vap import Water_Liquid_Vap

from icecream import ic

pressure_file = 'data/csv_files/H2O_PresSat.csv'
temperature_file = 'data/csv_files/H2O_TempSat.csv'
obj = None
try:
    obj = Water_Liquid_Vap(temperature_file)
    ic(obj.get_properties(100))
except Exception as e:
    ic(e)