import Air_Qual
from Air_Qual import *
from Output import *

def get_counties(data):  #get list of unique counties to check for in prompt
   ans = []
   for x in data:
       for y in x:
           if y[18] not in ans:
               ans.append(y[18])
   return ans

def get_sites(data):  #get list of unique local-sites to check for in prompt
   ans = []
   for x in data:
       for y in x:
           if y[7] not in ans:
               ans.append(y[7])
   return ans



def print_avg(split,filtered): #prints statement based on avg
    if Air_Qual.air_qual(split[1],filtered).CO2 > Air_Qual.air_qual(split[1],filtered).PM10 and Air_Qual.air_qual(split[1],filtered).CO2 > Air_Qual.air_qual(split[1],filtered).Ozone:
        print("\nCO2 is the largest avg contributor of pollution in the area. \nFossil Fuel use, Deforestation, and Industrial Processes are main causes of CO2 pollution. \nSwitching to renewable energy sources, planting trees and advocating for forest protection, and improving energy efficiency within industrial processes may help.\n\n-----------------------------------------------------------\n")
    elif Air_Qual.air_qual(split[1],filtered).Ozone > Air_Qual.air_qual(split[1],filtered).CO2 and Air_Qual.air_qual(split[1],filtered).Ozone > Air_Qual.air_qual(split[1],filtered).PM10:
        print("\nOzone is the largest avg contributor of pollution in the area. \nVehicle emissions, Industrial processes, and chemical solvents are main causes of Ozone pollution. \nPromoting Public transportation, implementing or advocating for stricter emission controls and cleaner technologies, and using eco friendly products may help.\n\n-----------------------------------------------------------\n")
    elif Air_Qual.air_qual(split[1],filtered).PM10 > Air_Qual.air_qual(split[1],filtered).CO2 and Air_Qual.air_qual(split[1],filtered).PM10 > Air_Qual.air_qual(split[1],filtered).Ozone:
        print("\nParticulate Matter is the largest avg contributor of pollution in the area. \nFossil fuel use, biomass burning, and construction are main causes of PM pollution. \nChoosing environment-healthy methods of transportation, reducing individual smoke emissions, and improving the cleanliness of construction sites may help.\n\n-----------------------------------------------------------\n")
    else:
        print("\nNo pollutant is the largest avg contributor.\n\n-----------------------------------------------------------\n")

def check(prompts,data):    #main caller function, goes through each prompt and calls the respective function
    counties = get_counties(data)  # loads all possible counties
    sites = get_sites(data)  # loads all possible sites
    filtered = data
    for prompt in prompts:
        if len(prompt.split(":")) > 1:  # if its an air_qual prompt
            split = prompt.split(":")
            print("Prompt: " + prompt)
            if split[1] in counties:  # input set as a county
                print("County: {} \n{}".format(split[1], air_qual(split[1],filtered)))
                print_avg(split,filtered)
            elif split[1] in sites:  # input set as a site
                print("Site: {} \n{}".format(split[1], air_qual(split[1],filtered)))
                print_avg(split,filtered)
        else:   #every other prompt
            print("Prompt: " + prompt)
            filtered = fil(prompt,filtered)
            most = most_pol(filtered)
            output(most)



def fil(prompt,data):   #depnending on prompt, finds avg, filers by counties, filters by local sites, and filters by month
    counties = get_counties(data)  # loads all possible counties
    sites = get_sites(data)  # loads all possible sites
    n_pm = data[0]    #new lists to filter each pollutant
    n_oz = data[1]
    n_co2 = data[2]
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

    return_data = [n_pm, n_oz, n_co2]
    return return_data



def most_pol(data):    #finds highest pollutant
    mp = 0
    mo = 0
    mc = 0
    if data[0][1:]:
        mp = max(int(p[6]) for p in data[0][1:])
    if data[1][1:]:
        mo = max(int(o[6]) for o in data[1][1:])
    if data[2][1:]:
        mc = max(int(c[6]) for c in data[2][1:])

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
    for t in thresh:
        if highest in t:
           hold = t

    ans_pm = []
    for p in data[0]:
        if int(p[6]) in hold and p[7] not in ans_pm:
           ans_pm.append(p[7])
    ans_oz = []
    for o in data[1]:
        if int(o[6]) in hold and o[7] not in ans_oz:
           ans_oz.append(o[7])
    ans_co2 = []
    for c in data[2]:
        if int(c[6]) in hold and c[7] not in ans_co2:
           ans_co2.append(c[7])

    maxi = [mp,mo,mc]
    ans = [ans_pm,ans_oz,ans_co2,maxi]
    return ans