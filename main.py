from Liquid_Vap import Liquid_Vap
from icecream import ic

# NH3 P and T, R22 P & T, and R134 P have unchanged units of kj, and Bars


H2O_Pres = 'data/csv_files/H2O_PresSat.csv'
H2O_Temp = 'data/csv_files/H2O_TempSat.csv'

R134_Temp = 'data/csv_files/R134a_TempSat.csv'
R134_Pres = 'data/csv_files/R134a_PresSat.csv'

NH3_Temp = 'data/csv_files/NH3_TempSat.csv'
NH3_Pres = 'data/csv_files/NH3_PresSat.csv'

R22_Temp = 'data/csv_files/R22_TempSat.csv'
R22_Pres = 'data/csv_files/R22_PresSat.csv'

obj = None
try:
    obj = Liquid_Vap(R134_Pres)
    ic(obj.MAX)
    ic(obj.MIN)
    ic(obj.get_properties(float(input('Enter property value: '))))
except Exception as e:
    ic(e)







#git push thermo