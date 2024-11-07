import csv
from grunnstoff import Grunnstoff
#import matplotlib.pyplot as plt

filnavn = "PeriodicTable.csv"                               # csv-filen
periodicTable = {}                                          # dictionary = {symbol; grunnstoffobjekt}

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    
    # hoppe over overskrifter
    overskrifter = next(filinnhold)
    print(overskrifter)

    for rad in filinnhold:
        # lage objekt, gi navn 
        g = Grunnstoff(*rad)                                #explode list to parameters
        periodicTable[g.symbol] = g

        print(g)
        #print(g.navn, g.atomnummer, type(g.elektronegativitet))

print(periodicTable.keys())


# forhold mellom nøytroner og atomnummer, graf
def noytronerProtonerForhold():
    for k, v in periodicTable.items():
        pass
    pass


# molarmasssekalkulator, input example "Na2SO4"
def molarMasseKalkulator(stoff):
    pass


