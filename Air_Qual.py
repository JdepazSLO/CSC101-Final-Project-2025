import DataFinder
class find_pollution:
    def __init__(self, Ozone, PM10, CO2, AQI):
        self.Ozone = Ozone
        self.PM10 = PM10
        self.CO2 = CO2
        self.AQI = AQI

    def __repr__(self):
        return 'Ozone: {} , PM10: {} , CO2: {}, Total AQI Average: {} '.format(self.Ozone, self.PM10, self.CO2, self.AQI)

def air_qual(Location):             #sorry for the long code you can make it better if you want
    PMaccumulator = 0               #but this creates a new class object of find_pollution and returns
    PMAirQuality = 0                 #the data on Ozone, PM10, CO2, and a total AQI of a specified location
    AirQuality = find_pollution(0,0,0,0)
    for x in DataFinder.PM_DataReport():
        if Location in x:
            PMAirQuality += int(x[6])
            PMaccumulator += 1
    try: AirQuality.PM10 = PMAirQuality / PMaccumulator
    except ZeroDivisionError: AirQuality.PM10 = "No Data Found"
    Ozoneaccumulator = 0
    OzoneAirQuality = 0
    for y in DataFinder.OZONE_DataReport():
        if Location in y:
            OzoneAirQuality += int(y[6])
            Ozoneaccumulator += 1
    try: AirQuality.Ozone = OzoneAirQuality / Ozoneaccumulator
    except ZeroDivisionError: AirQuality.Ozone = "No Data Found"
    CO2accumulator = 0
    CO2AirQuality = 0
    for z in DataFinder.CO2_DataReport():
        if Location in z:
            CO2AirQuality += int(z[6])
            CO2accumulator += 1
    try: AirQuality.CO2 = CO2AirQuality / CO2accumulator
    except ZeroDivisionError: AirQuality.CO2 = "No Data Found"
    try: AirQuality.AQI = (CO2AirQuality+OzoneAirQuality+PMAirQuality)/(CO2accumulator+Ozoneaccumulator+PMaccumulator)
    except ZeroDivisionError: return "No Data for Provided Input"



    return AirQuality