import csv
from grunnstoff import Grunnstoff
#import matplotlib.pyplot as plt

filnavn = "PeriodicTable.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)
  print(overskrifter)

  for rad in filinnhold:
    # lage objekt, gi navn 
    g = Grunnstoff(*rad)    #explode list to parameters

    print(g)
    #print(g.navn, g.atomnummer, type(g.elektronegativitet))

