class find_pollution:
    def __init__(self, PM10, Ozone, CO2, AQI):
        self.PM10 = PM10
        self.Ozone = Ozone
        self.CO2 = CO2
        self.AQI = AQI

    def __repr__(self):
        return 'PM10: {} , Ozone: {} , CO2: {}, Total AQI Average: {}'.format(self.PM10, self.Ozone, self.CO2, self.AQI)

    def __eq__(self, other):
        return (other is self or
                type(other) == find_pollution and
                self.PM10 == other.PM10 and
                self.Ozone == other.Ozone and
                self.CO2 == other.CO2 and
                self.AQI == other.AQI)

def air_qual(Location,data):       #creates a new class object of find_pollution and returns the data on Ozone, PM10, CO2,
    PMaccumulator = 0         #and a total AQI of a specified location
    PMAirQuality = 0
    AirQuality = find_pollution(0,0,0,0)
    for x in data[0]:
        if Location in x:
            PMAirQuality += int(x[6])
            PMaccumulator += 1
    try: AirQuality.PM10 = round(PMAirQuality / PMaccumulator,2)
    except ZeroDivisionError: AirQuality.PM10 = 0
    Ozoneaccumulator = 0
    OzoneAirQuality = 0
    for y in data[1]:
        if Location in y:
            OzoneAirQuality += int(y[6])
            Ozoneaccumulator += 1
    try: AirQuality.Ozone = round(OzoneAirQuality / Ozoneaccumulator,2)
    except ZeroDivisionError: AirQuality.Ozone = 0
    CO2accumulator = 0
    CO2AirQuality = 0
    for z in data[2]:
        if Location in z:
            CO2AirQuality += int(z[6])
            CO2accumulator += 1
    try: AirQuality.CO2 = round(CO2AirQuality / CO2accumulator,2)
    except ZeroDivisionError: AirQuality.CO2 = 0
    try: AirQuality.AQI = round((AirQuality.CO2+AirQuality.Ozone+AirQuality.PM10)/3,2)
    except ZeroDivisionError: return "No Data for Provided Input"


    return AirQuality