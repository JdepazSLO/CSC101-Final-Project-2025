import sys
import csv

#Open data files
def open_CO2data():
    try:
        CO2List = []                                                  #create empty list
        with open('CO2 DATA.csv', mode='r', newline='') as CO2DATA:   #open CO2 Data

            for row1 in CO2DATA:                                    #go through each row and append to CO2 List as a sublist
                 CO2List.append([row1])
            return CO2List
    except:
        print("Error: Could not retrieve CO2 data")

def open_OZONEdata():
    try:
        OZONEList = []                                                     #create empty list
        with open('OZONE DATA.csv', mode='r', newline='') as OZONEDATA:          #open ozone data


            for row2 in OZONEDATA:                                   #go through each row and append to Ozone List as a sublist
               OZONEList.append([row2])
            return OZONEList
    except:
        print("Error: Could not retrieve OZONE data")





#Input: Works by taking input text file and converting each word into its own element in a list. Find keywords through list and perform methods
def Find_Input():
    with open("Input", 'r') as f:    # Open Input File
        lines = [[x.rstrip('\n')] for x in f]   #remove lines from input file
        prompt = []                              #create prompt list
        for idx in range(len(lines)):
            words = lines[idx][0].split(" ")      #remove additional spaces and create each word into a keyword in a list
            prompt += words                       #add to prompt list
        return prompt



