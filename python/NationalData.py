##########################################################################################
# national data structure
##########################################################################################
class NationalData:
    def __init__(self):
        self.data = ""
        self.stato = ""
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

        #data calclulated from the other
        self.nuovi_tamponi = 0
        self.nuovi_morti = 0
        self.nuovi_tamponi_molecolari = 0
        self.nuovi_tamponi_antigenici = 0
        self.nuovi_positivi_tamponi_molecolari = 0
        self.nuovi_positivi_tamponi_antigenici = 0
        self.tp_ratio = 0.0

        
    def fillData(self,json):
        ##########################################################################################
        #fill the object class attributes; it fill up with the corrispective key 
        # into the JSON dataset, attributes and key that are called the same 
        # will automatically valued.
        ##########################################################################################
        for key in json:
            if hasattr(self, key):
                setattr(self,key,json[key])

    def fillCalculatedData(self, j_today, j_yesterday):
        ##########################################################################################
        # for the attributes that need some king of work you have to handle separately
        ##########################################################################################
        n_positivi = j_today["nuovi_positivi"]
        n_tamponi = j_today["tamponi"]-j_yesterday["tamponi"]
        ratio = round(((n_positivi)/(n_tamponi))*100,2)
        
        setattr(self,"nuovi_tamponi",n_tamponi)
        setattr(self,"nuovi_morti",j_today["deceduti"]-j_yesterday["deceduti"])
        setattr(self,"nuovi_tamponi_molecolari",j_today["tamponi_test_molecolare"]-j_yesterday["tamponi_test_molecolare"])
        setattr(self,"nuovi_tamponi_antigenici",j_today["tamponi_test_antigenico_rapido"]-j_yesterday["tamponi_test_antigenico_rapido"])
        setattr(self,"nuovi_positivi_tamponi_molecolari",j_today["totale_positivi_test_molecolare"]-j_yesterday["totale_positivi_test_molecolare"])
        setattr(self,"nuovi_positivi_tamponi_antigenici",j_today["totale_positivi_test_antigenico_rapido"]-j_yesterday["totale_positivi_test_antigenico_rapido"])
        setattr(self,"tp_ratio",ratio)