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
   n_pm = []    #new lists to filter each pollutant
   n_oz = []
   n_co2 = []
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
           for p in pm:
               if p[18] == prompt and p not in n_pm:
                   n_pm.append(p)
                   if int(p[6]) > mp:
                       mp = int(p[6])
           for o in oz:
               if o[18] == prompt and o not in n_oz:
                   n_oz.append(o)
                   if int(o[6]) > mo:
                       mo = int(o[6])
           for c in co2:
               if c[18] == prompt and c not in n_co2:
                   n_co2.append(c)
                   if int(c[6]) > mc:
                       mc = int(c[6])
       elif prompt in sites:    #site filter
           for p in pm:
               if p[7] == prompt and p not in n_pm:
                   n_pm.append(p)
                   if int(p[6]) > mp:
                       mp = int(p[6])
           for o in oz:
               if o[7] == prompt and o not in n_oz:
                   n_oz.append(o)
                   if int(o[6]) > mo:
                       mo = int(o[6])
           for c in co2:
               if c[7] == prompt and c not in n_co2:
                   n_co2.append(c)
                   if int(c[6]) > mc:
                       mc = int(c[6])
       elif str(prompt) in ["01","02","03","04","05","06","07","08","09","10","11","12"]:   #month filter
           for p in pm:
               if p[0].split("/")[0] == str(prompt) and p not in n_pm:
                   n_pm.append(p)
                   if int(p[6]) > mp:
                       mp = int(p[6])
           for o in oz:
               if o[0].split("/")[0] == str(prompt) and o not in n_oz:
                   n_oz.append(o)
                   if int(o[6]) > mo:
                       mo = int(o[6])
           for c in co2:
               if c[0].split("/")[0] == str(prompt) and c not in n_co2:
                   n_co2.append(c)
                   if int(c[6]) > mc:
                       mc = int(c[6])

   most_pol(n_pm, n_oz, n_co2, mp, mo, mc)  #call to find highest pollutant


def most_pol(pm, oz, co2, mp, mo, mc):    #finds highest pollutant
   ans_pm = []  #ans: filtered lists containing the data with the highest AQI
   ans_oz = []
   ans_co2 = []
   mp = mp  #imported from last function
   mo = mo
   mc = mc
   for i in range(len(pm)):
       if int(pm[i][6]) == mp and pm[i][7] not in ans_pm:
           ans_pm.append(pm[i][7])

   for i in range(len(oz)):
       if int(oz[i][6]) == mo and oz[i][7] not in ans_oz:
           ans_oz.append(oz[i][7])

   for i in range(len(co2)):
       if int(co2[i][6]) == mc and co2[i][7] not in ans_co2:
           ans_co2.append(co2[i][7])
   output(ans_pm, ans_oz, ans_co2,mp, mo, mc)   #call for final print