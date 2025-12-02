from Air_Qual import *
from Output import *

def get_counties(ls1,ls2,ls3):  #get list of unique counties to check for prompt
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

def get_sites(ls1,ls2,ls3):  #get list of unique local-sites to check for prompt
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


#prompt example:
#
def fil(prompts, pm, oz,co2):   #month, local site, find avg
   n_pm = []
   n_oz = []
   n_co2 = []
   mp = 0   #most pm
   mo = 0   #most oz
   mc = 0   #most co2
   for prompt in prompts:
       counties = get_counties(pm, oz, co2) #make more variables for potential filters
       sites = get_sites(pm, oz, co2)
       if len(prompt.split(":")) > 1:
           if prompt.split(":")[0] == "air_qual":
               print(air_qual(prompt.split(":")[1]))
               exit(1)

       if prompt in counties:
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
       elif prompt in sites:
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
       elif str(prompt) in ["01","02","03","04","05","06","07","08","09","10","11","12"]:
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

   most_pol(n_pm, n_oz, n_co2, mp, mo, mc)


def most_pol(pm,oz,co2,mp, mo, mc):    #how many times each pollutant is the highest pollution
   ans_pm = []  #if count_pm is greatest, return the highest pm objects
   ans_oz = []
   ans_co2 = []
   mp = mp
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
   output(ans_pm, ans_oz, ans_co2,mp, mo, mc)