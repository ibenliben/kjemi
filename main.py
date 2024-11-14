import csv
import time
from grunnstoff import Grunnstoff
import matplotlib.pyplot as plt


filnavn = "PeriodicTable.csv"                         # csv-filen
periodicTable = {}                                    # dictionary = {symbol; grunnstoffobjekt}

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    
    # hoppe over overskrifter
    overskrifter = next(filinnhold)
    print(overskrifter)

    for rad in filinnhold:
        # lage objekt, gi navn 
        g = Grunnstoff(*rad)                                #explode list to parameters
        periodicTable[g.symbol] = g

# meny
def print_meny():
    print("*"*25)
    print("Kjemi".center(20))
    print("*"*25)
    print("1. Se graf for forhold mellom nøytroner \n   og protoner hos stabile kjerner")
    print("")
    print("2. Omregning fra masse til mol")
    print("")
    print("3. Omregning fra mol til antall partikler")
    print("")
    print("4. Se forhold mellom elektronegativitet og atomradius")
    print("")
    print("5. Finn molarmasse for molekyl")
    print("")
    print("6. Gå ut")
    print("*"*25)
    tall = int(input("Hva vil du gjøre? (1-6): "))
    print("*"*25)
    return tall


""" GRAFPLOT """
# forhold mellom nøytroner og atomnummer, graf
x_protontall = []
y_noytrontall = []
def noytroner_protoner():
    for key, grunnstoff in periodicTable.items():
        x_protontall.append(grunnstoff.atomnummer)
        y_noytrontall.append(grunnstoff.noytron)
# noytroner_protoner()

# lage rett linje for sammenlikning
x_rett = []
y_rett = []
def rett_linje():
    for i in range(170):
        x_rett.append(i)
        y_rett.append(i)
# rett_linje()

def plot_noytron_proton_graf():
    plt.plot(x_rett, y_rett, color = "steelblue", label = "Z = N")
    plt.scatter(x_protontall, y_noytrontall, color = "r", s = 10)
    plt.xlabel("Antall protoner $Z$")
    plt.ylabel("Antall nøytroner $N$")
    plt.title("Forholdet mellom protontall og nøytrontall hos stabile kjerner")
    plt.legend(loc = "upper left")
    plt.show()
# plot_noytron_proton_graf()


# molarmasssekalkulator, input example "Na2SO4"
def molar_masse_kalkulator(stoff):
    pass




""" SVAR PÅ BRUKER INPUT """
def finn_grunnstoff(symbol):
    return periodicTable.get(symbol)

def finn_oppgave(tall):
    if tall == 1:
        noytroner_protoner()
        rett_linje()
        plot_noytron_proton_graf()

    elif tall == 2:
        bruker_symbol = input("Hvilket grunnstoff har du? Skriv symbol: ").capitalize()
        grunnstoff = finn_grunnstoff(bruker_symbol)
        if grunnstoff:
            m_verdi = int(input("Hvor mange gram har du?: "))
            print(grunnstoff.mol_fra_masse(m_verdi))
        else:
            print("Grunnstoffet ble ikke funnet.")

    elif tall == 3:
        bruker_symbol = input("Hvilket grunnstoff har du? Skriv symbol: ").capitalize()
        grunnstoff = finn_grunnstoff(bruker_symbol)
        if grunnstoff:
            mol = int(input("Hvor mange mol har du?: "))
            print(grunnstoff.mol_til_partikler(mol))
        else:
            print("Grunnstoffet ble ikke funnet.")
            
    elif tall == 4:
        pass
    elif tall == 5:
        pass

tall = 0
while tall != 6:
    tall = print_meny()
    if tall != 6:
        finn_oppgave(tall)
        print("")
        time.sleep(3)
    else:
        print("Avslutter programmet...")
        print("")
        break 
    
