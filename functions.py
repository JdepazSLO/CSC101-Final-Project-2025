import Air_Qual
from Air_Qual import *
from Output import *

def get_counties(ls1,ls2,ls3):  #get list of unique counties to check for in prompt
   ans = []
   for i in range(1,len(ls1)):
       if ls1[i][18] not in ans:
           ans.append(ls1[i][18])
   for i in range(1,len(ls2)):
       if ls2[i][18] not in ans:
           ans.append(ls2[i][18])
   for i in range(1,len(ls3)):
       if ls3[i][18] not in ans:
           ans.append(ls3[i][18])
   return ans

def get_sites(ls1,ls2,ls3):  #get list of unique local-sites to check for in prompt
   ans = []
   for i in range(1,len(ls1)):
       if ls1[i][7] not in ans:
           ans.append(ls1[i][7])
   for i in range(1,len(ls2)):
       if ls2[i][7] not in ans:
           ans.append(ls2[i][7])
   for i in range(1,len(ls3)):
       if ls3[i][7] not in ans:
           ans.append(ls3[i][7])
   return ans



def fil(prompts, pm, oz,co2):   #finds avg, filers by counties, filters by local sites, and filters by month
   n_pm = pm    #new lists to filter each pollutant
   n_oz = oz
   n_co2 = co2
   mp = 0   #most: used to track the highest possible AQI (finds the highest pollutant later)
   mo = 0   #most oz
   mc = 0   #most co2
   for prompt in prompts:
       counties = get_counties(pm, oz, co2) #all possible counties
       sites = get_sites(pm, oz, co2)   #all possible local sites
       if len(prompt.split(":")) > 1: #if its an air_qual call
           if prompt.split(":")[0] == "air_qual":
               if prompt.split(":")[1] in counties:
                    print("County: {} \n{}".format(prompt.split(":")[1], air_qual(prompt.split(":")[1])))
                    if Air_Qual.air_qual(prompt.split(":")[1]).CO2 > Air_Qual.air_qual(prompt.split(":")[1]).Ozone and Air_Qual.air_qual(prompt.split(":")[1]).CO2 > Air_Qual.air_qual(prompt.split(":")[1]).PM10:
                        print("\nCO2 is the largest avg contributor of pollution in this county. \nFossil Fuel use, Deforestation, and Industrial Processes are main causes of CO2 pollution. \nSwitching to renewable energy sources, planting trees and advocating for forest protection, and improving energy efficiency within industrial processes may help.\n\n-----------------------------------------------------------\n")
                    elif Air_Qual.air_qual(prompt.split(":")[1]).Ozone > Air_Qual.air_qual(prompt.split(":")[1]).CO2 and Air_Qual.air_qual(prompt.split(":")[1]).Ozone > Air_Qual.air_qual(prompt.split(":")[1]).PM10:
                        print("\nOzone is the largest avg contributor of pollution in this county. \nVehicle emissions, Industrial processes, and chemical solvents are main causes of Ozone pollution. \nPromoting Public transportation, implementing or advocating for stricter emission controls and cleaner technologies, and using eco friendly products may help.\n\n-----------------------------------------------------------\n")
                    elif Air_Qual.air_qual(prompt.split(":")[1]).PM10 > Air_Qual.air_qual(prompt.split(":")[1]).CO2 and Air_Qual.air_qual(prompt.split(":")[1]).PM10 > Air_Qual.air_qual(prompt.split(":")[1]).Ozone:
                        print("\n Particulate Matter is the largest avg contributor of pollution in the county\nFossil Fuel use, Deforestation, and Industrial Processes are main causes of CO2 pollution. \nSwitching to renewable energy sources, planting trees and advocating for forest protection, and improving energy efficiency within industrial processes may help.\n\n-----------------------------------------------------------\n")
               elif prompt.split(":")[1] in sites:
                    print("Site: {} \n{}".format(prompt.split(":")[1], air_qual(prompt.split(":")[1])))
                    if Air_Qual.air_qual(prompt.split(":")[1]).CO2 > Air_Qual.air_qual(prompt.split(":")[1]).Ozone and Air_Qual.air_qual(prompt.split(":")[1]).CO2 > Air_Qual.air_qual(prompt.split(":")[1]).PM10:
                        print("\nCO2 is the largest avg contributor of pollution in this site. \nFossil Fuel use, Deforestation, and Industrial Processes are main causes of CO2 pollution. \nSwitching to renewable energy sources, planting trees and advocating for forest protection, and improving energy efficiency within industrial processes may help.\n\n-----------------------------------------------------------\n")
                    elif Air_Qual.air_qual(prompt.split(":")[1]).Ozone > Air_Qual.air_qual(prompt.split(":")[1]).CO2 and Air_Qual.air_qual(prompt.split(":")[1]).Ozone > Air_Qual.air_qual(prompt.split(":")[1]).PM10:
                        print("\nOzone is the largest avg contributor of pollution in this site. \nVehicle emissions, Industrial processes, and chemical solvents are main causes of Ozone pollution. \nPromoting Public transportation, implementing or advocating for stricter emission controls and cleaner technologies, and using eco friendly products may help.\n\n-----------------------------------------------------------\n")
                    elif Air_Qual.air_qual(prompt.split(":")[1]).PM10 > Air_Qual.air_qual(prompt.split(":")[1]).CO2 and Air_Qual.air_qual(prompt.split(":")[1]).PM10 > Air_Qual.air_qual(prompt.split(":")[1]).Ozone:
                        print("\n Particulate Matter is the largest avg contributor of pollution in the site\nFossil Fuel use, Deforestation, and Industrial Processes are main causes of CO2 pollution. \nSwitching to renewable energy sources, planting trees and advocating for forest protection, and improving energy efficiency within industrial processes may help.\n\n-----------------------------------------------------------\n")

       if prompt in counties:   #county filter
           n_pm = [p for p in n_pm if p[18] == prompt]
           n_oz = [o for o in n_oz if o[18] == prompt]
           n_co2 = [c for c in n_co2 if c[18] == prompt]
       elif prompt in sites:    #site filter
           n_pm = [p for p in n_pm if p[7] == prompt]
           n_oz = [o for o in n_oz if o[7] == prompt]
           n_co2 = [c for c in n_co2 if c[7] == prompt]
       elif str(prompt) in ["01","02","03","04","05","06","07","08","09","10","11","12"]:   #month filter
           n_pm = [p for p in n_pm if p[0].split("/")[0] == str(prompt)]
           n_oz = [o for o in n_oz if o[0].split("/")[0] == str(prompt)]
           n_co2 = [c for c in n_co2 if c[0].split("/")[0] == str(prompt)]
       mp = max(int(p[6]) for p in n_pm[1:])
       mo = max(int(o[6]) for o in n_oz[1:])
       mc = max(int(c[6]) for c in n_co2[1:])
   most_pol(n_pm, n_oz, n_co2, mp, mo, mc)  #call to find highest pollutant


def most_pol(pm, oz, co2, mp, mo, mc):    #finds highest pollutant
   highest = max(mp,mo,mc)
   thresh = [
       range(1,50),
       range(51,100),
       range(101,150),
       range(151,200),
       range(201,300),
       range(301,500),
   ]
   hold = (0,0)
   if highest in thresh[0]:
       hold = thresh[0]
   elif highest in thresh[1]:
       hold = thresh[1]
   elif highest in thresh[2]:
       hold = thresh[2]
   elif highest in thresh[3]:
       hold = thresh[3]
   elif highest in thresh[4]:
       hold = thresh[4]
   elif highest in thresh[5]:
       hold = thresh[5]

   ans_pm = [p[7] for p in pm if int(p[6]) in hold]
   ans_oz = [o[7] for o in oz if int(o[6]) in hold]
   ans_co2 = [c[7] for c in co2 if int(c[6]) in hold]

   output(ans_pm, ans_oz, ans_co2,mp,mo,mc)   #call for final print