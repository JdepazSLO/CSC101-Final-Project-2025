from DataFinder import Find_Input, PM_DataReport, OZONE_DataReport, CO2_DataReport
from functions import *
if __name__ == '__main__':  #might not need comm. line

   #load all data
   PM_data = PM_DataReport()
   Ozone_data = OZONE_DataReport()
   CO2_data = CO2_DataReport()

   #get inputs
   prompts = Find_Input()

   #begins the functions
   fil(prompts, PM_data, Ozone_data, CO2_data)
