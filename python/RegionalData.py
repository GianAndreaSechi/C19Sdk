##########################################################################################
# regional data structure
##########################################################################################
class RegionalData:
    #region_list = ["Abruzzo","Basilicata","Calabria","Campania","Emilia-Romagna","Friuli Venezia Giulia","Lazio","Liguria","Lombardia","Marche","Molise","P.A. Bolzano","P.A. Trento","Piemonte","Puglia","Sardegna","Sicilia","Toscana","Umbria","Valle d'Aosta","Veneto"]
    def __init__(self):
        self.data = ""
        self.stato = ""
        self.codice_regione = ""
        self.denominazione_regione = ""
        self.lat = ""
        self.long = ""
        self.ricoverati_con_sintomi = 0
        self.terapia_intensiva = 0
        self.totale_ospedalizzati = 0
        self.isolamento_domiciliare = 0
        self.totale_positivi = 0
        self.variazione_totale_positivi = 0
        self.nuovi_positivi = 0
        self.dimessi_guariti = 0
        self.deceduti = 0
        self.casi_da_sospetto_diagnostico = 0
        self.casi_da_screening = 0
        self.totale_casi = 0
        self.tamponi = 0
        self.casi_testati = 0
        self.note = ""
        self.ingressi_terapia_intensiva = 0
        self.note_test = ""
        self.note_casi = ""
        self.totale_positivi_test_molecolare = 0
        self.totale_positivi_test_antigenico_rapido = 0
        self.tamponi_test_molecolare = 0
        self.tamponi_test_antigenico_rapido = 0
        self.codice_nuts_1 = 0
        self.codice_nuts_2 = 0

        #data calclulated from the other
        self.nuovi_tamponi = 0
        self.nuovi_morti = 0
        self.nuovi_tamponi_molecolari = 0
        self.nuovi_tamponi_antigenici = 0
        self.nuovi_positivi_tamponi_molecolari = 0
        self.nuovi_positivi_tamponi_antigenici = 0
        self.tp_ratio = 0.0

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

        if item_today["codice_regione"] == j_yesterday[index]["codice_regione"]: #check if the two json refer to the same regione code
            n_positivi = item_today['nuovi_positivi']
            n_tamponi = item_today["tamponi"]-j_yesterday[index]["tamponi"]
            ratio = round(((n_positivi)/(n_tamponi))*100,2)
        
            setattr(self,"nuovi_tamponi",n_tamponi)
            setattr(self,"nuovi_morti",item_today["deceduti"]-j_yesterday[index]["deceduti"])
            setattr(self,"nuovi_tamponi_molecolari",item_today["tamponi_test_molecolare"]-j_yesterday[index]["tamponi_test_molecolare"])
            setattr(self,"nuovi_tamponi_antigenici",item_today["tamponi_test_antigenico_rapido"]-j_yesterday[index]["tamponi_test_antigenico_rapido"])
            setattr(self,"nuovi_positivi_tamponi_molecolari",item_today["totale_positivi_test_molecolare"]-j_yesterday[index]["totale_positivi_test_molecolare"])
            setattr(self,"nuovi_positivi_tamponi_antigenici",item_today["totale_positivi_test_antigenico_rapido"]-j_yesterday[index]["totale_positivi_test_antigenico_rapido"])
            setattr(self,"tp_ratio",ratio)
        else:
            print("Regione non corrispondente")

            
        
    