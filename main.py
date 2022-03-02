from Water_Liquid_Vap_Temp import Water_Liquid_vap_Temp
from icecream import ic

obj = Water_Liquid_vap_Temp('data/csv_files/test1.csv')

#error whent T = 1*C
ic(obj.get_properties(111))

