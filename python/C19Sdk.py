import requests
from datetime import date, datetime, timedelta
from NationalData import NationalData
from RegionalData import RegionalData
from DistrictData import DistrictData

##########################################################################################
#list of endpoints can be choose
##########################################################################################
endpoint_choices = {
        "N": "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json",
        "R": "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json",
        "P": "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province.json",
        "L": "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json"
    
    }
def createJSON(dat, json):
    ##########################################################################################
    #This function is used to split the JSON file into a JSON with only certaind date data.
    ##########################################################################################
    j_object = []
    for item in json:
        item_date = datetime.strptime(item["data"][0:10],'%Y-%m-%d')
        if item_date == dat:
            j_object.append(item)
    return(j_object)

def formatData(data):
    ##########################################################################################
    #This function is used to format data into YYYY-MM-DD format.
    ##########################################################################################
    return datetime.strptime(str(data),'%Y-%m-%d').date()
def getLastUpdate():
    ##########################################################################################
    #This function is used to get the last dataset date update.
    ##########################################################################################
    date_response = requests.get(endpoint_choices["L"])
    date_json =  date_response.json()
    for item in date_json:
        last_update = formatData(item["data"][0:10])

    return last_update

##########################################################################################
#init data and choose correct endpoint
#also call the filling up function for the called object
##########################################################################################
class CovidData:
    def __init__(self, tipology="N"): 
        self.actual_type = tipology
        try:
            self.endpoint = endpoint_choices[self.actual_type]
        except:
            self.endpoint = "error"

        self.getData()
    
    def getData(self): 
        today = getLastUpdate() #get last update of dataset 
        yesterday = formatData(today) - timedelta(days=1) #get the day before last update of dataset
        
        #i choose the name of attributes are the same of the key name of json file retrieve so you can fill automatically.
        #any different variables/attributes that aren't in JSON Schema will be valued distinctly
        response = requests.get(self.endpoint)
        json =  response.json()

        if self.actual_type == "N":
            #setting data for National Dataset
            self.object_data = NationalData()
            self.object_data.fillData(json[len(json)-1])
            self.object_data.fillCalculatedData(json[len(json)-1],json[len(json)-2])
        elif self.actual_type == "R":
            #setting data for Regional Dataset
            j_today = createJSON(today, json)
            j_yesterday = createJSON(yesterday, json)
            
            self.object_data = []
            for index,item in enumerate(j_today):
                self.obj = RegionalData()
                self.obj.fillData(item,j_yesterday, index) #pass the index because the order seams to be the same for each date so, thanks to index i can access to yesterday reagion directly
                self.object_data.append(self.obj)
        else:
            #setting data for District Dataset
            j_today = createJSON(today, json)
            j_yesterday = createJSON(yesterday, json)

            self.object_data = []

            for index,item in enumerate(j_today):
                self.obj = DistrictData()
                self.obj.fillData(item,j_yesterday, index) #pass the index because the order seams to be the same for each date so, thanks to index i can access to yesterday reagion directly
                self.object_data.append(self.obj)
                
                
        
    
#used for testing directly into sdk
#if __name__ == "__main__":
    #n_data = CovidData("N")
    #r_data = CovidData("R") #a little bit slow because the dataset is huge and need a bit of time to be loaded
    #d_data = CovidData("P") #a little bit slow because the dataset is huge and need a bit of time to be loaded
