
dic_ans = {

    "safe" : "All of the air quality data returned from given prompts poses no health issues :)",
    "moderate" : "Worst local AQI:  {} level of {} (Moderate). \nAir Quality at this level is generally acceptable. However, there may be a risk for some people who are sensitive to air pollution. \n{} local site(s) have had this pollutant's air quality level:",
    "Unhealthy for Sensitive Groups" : "Worst local AQI: {} level of {} (Unhealthy for Sensitive Groups). \nMembers of sensitive groups may experience health effects. The general public is less likely to be affected. \n{} local site(s) have had this pollutant's air quality level:",
    "Unhealthy" : "Worst local AQI:  {} level of {} (Unhealthy). \nSome members of the general public may experience health affects. Members of sensitive groups may experience serious health effects. \n{} local site(s) have had this pollutant's air quality level:",
    "Very Unhealthy" : "Worst local AQI:  {} level of {} (Very Unhealthy). \nAir Quality of this level is a public health risk for the entirety of the general public \n{} local site(s) have had this pollutant's air quality level:",
    "Hazardous" : "Worst local AQI:  {} level of {} (Hazardous). \nAir Quality of this level poses serious Hazard. These are considered emergency conditions and anyone who is exposed is likely to be affected. \n{} local site(s) have had this pollutant's air quality level:"
}
def output(lst):  #which pollution needs to be addressed? (used for final print suggestion)
#mp, mo, mc -> highest aqi of each pollutant
#count -> frequency of highest aqi in each dataset
#ans - > list of each element with highest aqi
    dic_output = {lst[3][0] : [lst[3][0], lst[0],"Particulate Matter", "\nFossil fuel use, biomass burning, and construction are main causes of PM pollution. \nChoosing environment-healthy methods of transportation, reducing individual smoke emissions, and improving the cleanliness of construction sites may help.\n\n"] ,
                  lst[3][1] : [lst[3][1], lst[1],"Ozone", "\nVehicle emissions, Industrial processes, and chemical solvents are main causes of Ozone pollution. \nPromoting Public transportation, implementing or advocating for stricter emission controls and cleaner technologies, and using eco friendly products may help.\n\n"],
                  lst[3][2] : [lst[3][2], lst[2],"Carbon Dioxide", "\nFossil Fuel use, Deforestation, and Industrial Processes are main causes of CO2 pollution. \nSwitching to renewable energy sources, planting trees and advocating for forest protection, and improving energy efficiency within industrial processes may help\n\n"]}
    highestcount = max(lst[3])  #finds the absolute biggest AQI
    if dic_output[highestcount][0] <= 50:   #AQI indicators
        print (dic_ans["safe"])
        print ("Highest AQI: {} of {} (Great!)\n\n------------------------------------".format(dic_output[highestcount][2], dic_output[highestcount][0]))
    if dic_output[highestcount][0] > 50 and dic_output[highestcount][0] <= 100:
        print (dic_ans["moderate"].format(dic_output[highestcount][2], dic_output[highestcount][0],len(dic_output[highestcount][1])))
        print (dic_output[highestcount][1])
        print ("\n---------------------------------------")
        print (dic_output[highestcount][3])
    if dic_output[highestcount][0] > 100 and dic_output[highestcount][0] <= 150:
        print (dic_ans["Unhealthy for Sensitive Groups"].format(dic_output[highestcount][2], dic_output[highestcount][0],len(dic_output[highestcount][1])))
        print (dic_output[highestcount][1])
        print ("\n---------------------------------------")
        print (dic_output[highestcount][3])
    if dic_output[highestcount][0] > 150 and dic_output[highestcount][0] <= 200:
        print (dic_ans["Unhealthy"].format(dic_output[highestcount][2], dic_output[highestcount][0],len(dic_output[highestcount][1])))
        print (dic_output[highestcount][1])
        print ("\n---------------------------------------")
        print (dic_output[highestcount][3])
    if dic_output[highestcount][0] > 200 and dic_output[highestcount][0] <= 300:
        print (dic_ans["Very Unhealthy"].format(dic_output[highestcount][2], dic_output[highestcount][0],len(dic_output[highestcount][1])))
        print (dic_output[highestcount][1])
        print ("\n---------------------------------------")
        print (dic_output[highestcount][3])
    if dic_output[highestcount][0] > 300:
        print (dic_ans["Hazardous"].format(dic_output[highestcount][2], dic_output[highestcount][0],len(dic_output[highestcount][1])))
        print (dic_output[highestcount][1])
        print ("\n---------------------------------------")
        print (dic_output[highestcount][3])








