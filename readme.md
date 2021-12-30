# pcm-dpc covid-19 parser

This is a simple parser, written in python, to simplify the access to the COVID-19 dataset provided by Italian Government (https://github.com/pcm-dpc/COVID-19).

The usage is simple.
You only need to download and import the file:
```
import sys
sys.path.append('/.../app_path/C19Sdk/Python')
import C19Sdk
```

To retrive the data you have to use this syntax:
```
# the name of variable can be whatever you want
# the parameter is N for default or it has to be (N, R, D)
n_data = CovidData("N") 
r_data = CovidData("R")
d_data = CovidData("P")
```

After that you can retrive the information using this sintax:
|  Key   |      Endpoint      |  Output |
|------------------|:-------------:|------:|
| N |  National Data | NationalData Object |
| R |    Regional Data   |   List of RegionalData Objects |
| D | District Data |    List of DistrictData Objects |
| L | Used only to get the last update date |  YYYY-mm-dd date format |



According to the pcm-dpc dataset, the name of the attributes in the object are keep in italian in order to have a directly corrispondation with the dataset.
## legenda:
✅ this means the field are directly retrieve by the pcm-dpc dataset
❌ this means the field are calculated from data of the pcm-dpc dataset.

## NationalData:

|  Attributes   |      Description      |  In original dataset |
|------------------|:-------------:|---------------:|
| data | date when the data item was collected | ✅ |
| stato | Nation of data (ITA) | ✅ |
| ricoverati_con_sintomi | hospitalized with symptoms |   ✅ |
| terapia_intensiva | intensive care |    ✅ |
| totale_ospedalizzati| total hospitalized |    ✅ |
| isolamento_domiciliare | home isolation | ✅ |
| totale_positivi | total positives |   ✅ |
| variazione_totale_positivi | positive difference healed |    ✅ |
| nuovi_positivi| new positives |    ✅ |
| dimessi_guariti | healed | ✅ |
| deceduti | died |   ✅ |
| casi_da_sospetto_diagnostico | suspicious cases | ✅ |
| casi_da_screening| screening cases | ✅ |
| totale_casi |  total cases  | ✅ |
| tamponi | swabs | ✅ |
| casi_testati | tested cases | ✅ |
| note | note | ✅ |
| ingressi_terapia_intensiva | intensive care entrace  | ✅ |
| note_test | test note | ✅ |
| note_casi | cases note | ✅ |
| nuovi_tamponi| new swabs | ❌ |
| nuovi_morti |  new died | ❌ |
| nuovi_tamponi_molecolari | new molecolar swabs | ❌ |
| nuovi_tamponi_antigenici | new antigenic swabs | ❌ |
| nuovi_positivi_tamponi_molecolari| new positives by molecular swabs | ❌ |
| nuovi_positivi_tamponi_antigenici| new positives by antigenic swabs | ❌ |
| tp_ratio | positives/swans ratio | ❌ |

## RegionalData:

|  Attributes   |      Description      |  In original dataset |
|------------------|:-------------:|--------------:|
| data | date when the data item was collected | ✅ |
| stato | Nation of data (ITA) | ✅ |
| codice_regione | ISTAT code referred of the region | ✅ |
| denominazione_regione | Name of the region | ✅ |
| lat | Latidude | ✅ |
| long | Longitude | ✅ |
| ricoverati_con_sintomi | hospitalized with symptoms |   ✅ |
| terapia_intensiva | intensive care |    ✅ |
| totale_ospedalizzati| total hospitalized |    ✅ |
| isolamento_domiciliare | home isolation | ✅ |
| totale_positivi | total positives |   ✅ |
| variazione_totale_positivi | positive difference healed |  ✅ |
| nuovi_positivi| new positives |    ✅ |
| dimessi_guariti | healed | ✅ |
| deceduti | died |   ✅ |
| casi_da_sospetto_diagnostico | suspicious cases | ✅ |
| casi_da_screening| screening cases | ✅ |
| totale_casi |  total cases  | ✅ |
| tamponi | swabs | ✅ |
| casi_testati | tested cases | ✅ |
| note | note | ✅ |
| ingressi_terapia_intensiva | intensive care entrace  | ✅ |
| note_test | test note | ✅ |
| note_casi | cases note | ✅ |
| totale_positivi_test_molecolare | total positives by molecular swabs | ✅ |
| totale_positivi_test_antigenico_rapido | total positives by antigenic swabs | ✅ |
| tamponi_test_molecolare | total molecular swabs | ✅ |
| tamponi_test_antigenico_rapido | total antigenic swabs | ✅ |
| codice_nuts_1 |  | ✅ |
| codice_nuts_2 |  | ✅ |
| nuovi_tamponi| new swabs | ❌ |
| nuovi_morti |  new died | ❌ |
| nuovi_tamponi_molecolari | new molecolar swabs | ❌ |
| nuovi_tamponi_antigenici | new antigenic swabs | ❌ |
| nuovi_positivi_tamponi_molecolari| new positives by molecular swabs | ❌ |
| nuovi_positivi_tamponi_antigenici| new positives by antigenic swabs | ❌ |
| tp_ratio | positives/swans ratio | ❌ |


## DistrictData:

|  Attributes   |      Description      |  In original dataset |
|------------------|:-------------:|------:|
| data | date when the data item was collected | ✅ |
| codice_regione | code of the region | ✅ |
| denominazione_regione | Name of the region | ✅ |
| codice_provincia | code of the district |   ✅ |
| denominazione_provincia | district denomination |    ✅ |
| sigla_provincia | district abbreviation | ✅ |
| lat | Latidude | ✅ |
| long | Longitude | ✅ |
| note | note | ✅ |
| totale_positivi | total positives |   ✅ |
| codice_nuts_1 |  |  ✅ |
| codice_nuts_2 |  |  ✅ |
| codice_nuts_3 |  |  ✅ |
| nuovi_casi| new cases | ❌ |
