from Air_Qual import air_qual
from DataFinder import Find_Input, PM_DataReport, OZONE_DataReport, CO2_DataReport
from functions import *
#PM_data = PM_DataReport()
#print(PM_data) #testing

def test():
    ans = []
    ans.append(["01/01/2025","AirNow","060010009","1","0.01","ppm","9","Oakland","24","100.0000","44201","Ozone","","41860","San Francisco-Oakland-Hayward, CA","06","California","001","Alameda","37.743065","-122.169935"])
    ans.append(["04/09/2025","AQS","060070008","1","0.044","ppm","41","Chico-East Avenue","17","100.0000","44201","Ozone","087","17020","Chico, CA","06","California","007","Butte","39.76168","-121.84047"])
    return ans
if __name__ == '__main__':  #might not need comm. line




   #load all data
   PM_data = PM_DataReport()
   Ozone_data = OZONE_DataReport()
   CO2_data = CO2_DataReport()




   #get inputs
   prompts = Find_Input()


   fil(prompts, PM_data, Ozone_data, CO2_data)
