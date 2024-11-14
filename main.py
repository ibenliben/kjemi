import csv
from grunnstoff import Grunnstoff
import matplotlib.pyplot as plt

filnavn = "PeriodicTable.csv"                         # csv-filen
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

        #print(g)
        #print(g.navn, g.atomnummer, type(g.elektronegativitet))

#print(periodicTable.keys())

# meny
def printMeny():
    print("*"*25)
    print("Kjemi".center(20))
    print("*"*25)
    print("1. Se graf for forhold mellom nøytroner \n   og protoner hos stabile kjerner")
    print("")
    print("2. Omregning fra masse til mol")
    print("")
    print("3. Omregning fra mol til antall partikler")
    print("")
    print("4. ")
    print("")
    print("5. ")
    print("")
    print("6. Gå ut")
    print("*"*25)
    print("Hva vil du gjøre? (1-6):")
    print("*"*25)
printMeny()


""" GRAFPLOT """
# forhold mellom nøytroner og atomnummer, graf
x_protontall = []
y_noytrontall = []
def noytronerProtoner():
    for key, grunnstoff in periodicTable.items():
        x_protontall.append(grunnstoff.atomnummer)
        y_noytrontall.append(grunnstoff.noytron)
noytronerProtoner()

# lage rett linje for sammenlikning
x_rett = []
y_rett = []
def rettLinje():
    for i in range(170):
        x_rett.append(i)
        y_rett.append(i)
rettLinje()

def plotNoytronProtonGraf():
    plt.plot(x_rett, y_rett, color = "steelblue", label = "Z = N")
    plt.scatter(x_protontall, y_noytrontall, color = "r", s = 10)
    plt.xlabel("Antall protoner $Z$")
    plt.ylabel("Antall nøytroner $N$")
    plt.title("Forholdet mellom protontall og nøytrontall hos stabile kjerner")
    plt.legend(loc = "upper left")
    plt.show()



# molarmasssekalkulator, input example "Na2SO4"
def molarMasseKalkulator(stoff):
    pass


