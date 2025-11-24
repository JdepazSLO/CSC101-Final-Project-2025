
import csv








#Input: Works by taking input text file and converting each word into its own element in a list. Find keywords through list and perform methods
def Find_Input():
    with open("Input", 'r') as f:    # Open Input File
        lines = [[x.rstrip('\n')] for x in f]   #remove lines from input file
        prompt = []                              #create prompt list
        for idx in range(len(lines)):
            words = lines[idx][0].split(" ")      #remove additional spaces and create each word into a keyword in a list
            prompt += words                       #add to prompt list
        return prompt



#Open Data Files

def PM_DataReport():               #Returns PM Dataset as a large list with sublists containing each element
    try:
        with open('PM10 DATA.csv', 'r') as f:
            PMreader = csv.reader(f)
            return [row for row in PMreader]
    except:
        print("Error: Could not retrieve Particulate Matter data")



def OZONE_DataReport():               #Returns OZONE Dataset as a large list with sublists containing each element
    try:
        with open('OZONE DATA.csv', 'r') as f:
            OZONEreader = csv.reader(f)
            return [row for row in OZONEreader]
    except:
        print("Error: Could not retrieve Ozone data")


def CO2_DataReport():               #Returns CO2 Dataset as a large list with sublists containing each element
    try:
        with open('CO2 DATA.csv', 'r') as f:
            CO2reader = csv.reader(f)
            return [row for row in CO2reader]
    except:
        print("Error: Could not retrieve Carbon Monoxide data")





