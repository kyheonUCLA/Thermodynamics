from Water_Liquid_Vap_Pressure import Water_Liquid_Vap_Pressure
from Water_Liquid_Vap_Temp import Water_Liquid_Vap_Temp
from Water_Liquid_Vap import Water_Liquid_Vap

from icecream import ic

H2O_pressure_file = 'data/csv_files/H2O_PresSat.csv'
H2O_temperature_file = 'data/csv_files/H2O_TempSat.csv'
R134_Temperature_file = 'data/csv_files/R134_TempSat.csv'

obj = None
try:
    obj = Water_Liquid_Vap(R134_Temperature_file)
    ic(obj.get_properties(int(input('Enter property value: '))))
except Exception as e:
    ic(e)







#git push thermo