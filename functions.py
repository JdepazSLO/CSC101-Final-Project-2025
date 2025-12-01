from Air_Qual import *

def get_counties(ls1,ls2,ls3):  #get list of unique counties to check for prompt
   ans = []
   for i in range(len(ls1)):
       if ls1[i][19] not in ans:
           ans.append(ls1[i][19])
   for i in range(len(ls2)):
       if ls2[i][19] not in ans:
           ans.append(ls2[i][19])
   for i in range(len(ls3)):
       if ls3[i][19] not in ans:
           ans.append(ls3[i][19])
   return ans

def get_sites(ls1,ls2,ls3):  #get list of unique local-sites to check for prompt
   ans = []
   for i in range(len(ls1)):
       if ls1[i][8] not in ans:
           ans.append(ls1[i][8])
   for i in range(len(ls2)):
       if ls2[i][8] not in ans:
           ans.append(ls2[i][8])
   for i in range(len(ls3)):
       if ls3[i][8] not in ans:
           ans.append(ls3[i][8])
   return ans


#prompt example:
#
def fil(prompts, pm, oz,co2):
   n_pm = []
   n_oz = []
   n_co2 = []
   m = 0   #month, local site, find avg
   for prompt in prompts:
       counties = get_counties(pm, oz, co2) #make more variables for potential filters
       sites = get_sites(pm, oz, co2)
       if len(prompt.split(":") > 1):
           if prompt[0] == "air_qual":
               print(air_qual(prompt[1]))

       if prompt in counties:
           for p in pm:
               if p[19] == prompt and p not in n_pm:
                   n_pm.append(p)
                   if p[7] > m:
                       m = p[7]
           for o in oz:
               if o[19] == prompt and o not in n_oz:
                   n_oz.append(o)
                   if o[7] > m:
                       m = o[7]
           for c in co2:
               if c[19] == prompt and c not in n_co2:
                   n_co2.append(c)
                   if c[7] > m:
                       m = c[7]
       elif prompt in sites:
           for p in pm:
               if p[8] == prompt and p not in n_pm:
                   n_pm.append(p)
                   if p[7] > m:
                       m = p[7]
           for o in oz:
               if o[8] == prompt and o not in n_oz:
                   n_oz.append(o)
                   if o[7] > m:
                       m = o[7]
           for c in co2:
               if c[8] == prompt and c not in n_co2:
                   n_co2.append(c)
                   if c[7] > m:
                       m = c[7]
       elif str(prompt) in ["01","02","03","04","05","06","07","08","09","10","11","12"]:
           for p in pm:
               if p[0].split("/")[0] == str(prompt) and p not in n_pm:
                   n_pm.append(p)
                   if p[7] > m:
                       m = p[7]
           for o in oz:
               if o[0].split("/")[0] == str(prompt) and o not in n_oz:
                   n_oz.append(o)
                   if o[7] > m:
                       m = o[7]
           for c in co2:
               if c[0].split("/")[0] == str(prompt) and c not in n_co2:
                   n_co2.append(c)
                   if c[7] > m:
                       m = c[7]

   most_pol(n_pm, n_oz, n_co2, m)


def most_pol(pm,oz,co2,m):    #which ones are the most polluted
   ans = []
   m = m
   for i in range(len(pm)):
       if pm[i][7] == m and pm[i] not in ans:
           ans.append(pm[i])
   for i in range(len(oz)):
       if oz[i][7] == m and oz[i] not in ans:
           ans.append(oz[i])
   for i in range(len(co2)):
       if co2[i][7] == m and co2[i] not in ans:
           ans.append(co2[i])
   which_pol(ans,m)
#need a middle function to find highest pollutant

def which_pol(ans,m): #threshold - pm:
    pol = 0
    m = m
    for a in ans:





dic_ans = {

    "safe" : ["All of the air quality data returned from given prompts poses no health issues :)"],
    "moderate" : ["Worst air quality is {} (moderate). The local sites with this air quality are {}"],

}

def output(lst,m):  #which pollution needs to be addressed? (used for final print suggestion)
    name_list = []
    if m <= 50:
        print(dic_ans["safe"])
    else:
        for x in lst and x[8] not in name_list:
            name_list.append(x[8])
        if m <= 100:
            print(dic_ans["moderate"].format(m,name_list))
        elif m <= 150:

        elif m <= 200:

        elif m <= 300:

        elif m <= 500:
