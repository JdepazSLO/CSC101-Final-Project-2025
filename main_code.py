from DataFinder import Find_Input, PM_DataReport, OZONE_DataReport, CO2_DataReport
from functions import *
if __name__ == '__main__':
    # load all data into one list
    def create_data():
        lst = []
        PM_data = PM_DataReport()
        lst.append(PM_data)
        Ozone_data = OZONE_DataReport()
        lst.append(Ozone_data)
        CO2_data = CO2_DataReport()
        lst.append(CO2_data)
        return lst


    data = create_data()


    #get inputs
    prompts = Find_Input()

    #begins the functions

    check(prompts,data)

