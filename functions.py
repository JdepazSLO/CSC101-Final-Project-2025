def get_counties(ls1,ls2,ls3):  #get list of counties to check for in comm. line
   ans = []
   for i in range(len(ls1)):
       if ls1[i] not in ans:
           ans.append(ls1[i])
   for i in range(len(ls2)):
       if ls2[i] not in ans:
           ans.append(ls2[i])
   for i in range(len(ls3)):
       if ls3[i] not in ans:
           ans.append(ls3[i])
   return ans


#prompt example:
#
def fil(prompts, pm, oz,co2):
   n_pm = []
   n_oz = []
   n_co2 = []
   m = 0   #month, day, local site, find avg
   for prompt in prompts:
       counties = get_counties(pm, oz, co2) #make more variables for potential filters
       if prompt in counties:
           for p in pm:
               if p[19] == prompt and p[19] not in n_pm:
                   n_pm.append(p)
                   if p[7] > m:
                       m = p[7]
           for o in oz:
               if o[19] == prompt and o[19] not in n_oz:
                   n_oz.append(o)
                   if o[7] > m:
                       m = o[7]
           for c in co2:
               if c[19] == prompt and c[19] not in n_co2:
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
   #which_pol(ans,m)
#need a middle function to find highest pollutant




# def which_pol(lst,m):  #which pollution needs to be addressed? (used for final print suggestion)
#     name_list = []
#     if m <= 50:
#         print("All of the air quality data returned from given prompts poses no health issues :)")
#     else:
#         for x in lst:
#             name_list.append(x[8])
#         if m <= 100:
#             print("Worst air quality is {} (moderate). The local sites with this air quality are {}".format(max,name_list))
#         elif m <= 150:
#
#         elif m <= 200:
#
#         elif m <= 300:
#
#         elif m <= 500:
