##########################################################################################
# district data structure
##########################################################################################
class DistrictData:
    def __init__(self):
        self.data = ""
        self.stato = ""
        self.codice_regione = ""
        self.denominazione_regione = ""
        self.codice_provincia = ""
        self.denominazione_provincia = ""
        self.sigla_provincia = ""
        self.lat = ""
        self.long = ""
        self.totale_casi = 0
        self.note = ""
        self.codice_nuts_1 = ""
        self.codice_nuts_2 = ""
        self.codice_nuts_3 = ""
        #data calclulated from the other
        self.nuovi_casi = 0
    
    def fillData(self,item_today, j_yesterday, index):
        ##########################################################################################
        #fill the object class attributes
        # 1. it fill up with the corrispective key into the JSON dataset, attributes and key that
        #    are called the same will automatically valued.
        # 2. for the attributes that need some king of work you have to handle separately
        ##########################################################################################
        for key in item_today:
            if hasattr(self, key):
                setattr(self,key,item_today[key])

        if item_today["codice_provincia"] == j_yesterday[index]["codice_provincia"]: #check if the two json refer to the same regione code
            n_positivi = item_today["totale_casi"]-j_yesterday[index]["totale_casi"]
        
            setattr(self,"nuovi_casi",n_positivi)
        else:
            print("Provincia non corrispondente")