import csv
import time
from grunnstoff import Grunnstoff
from kjemi_utils import fra_navn_til_dict
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
    print("1. Omregning fra masse til mol")
    print("")
    print("2. Omregning fra mol til antall partikler")
    print("")
    print("3. Finn molarmasse for molekyl")
    print("")
    print("4. Bindingsbonanza")
    print("")
    print("5. Se forhold mellom elektronegativitet og atomradius")
    print("")
    print("6. Se graf for forhold mellom nøytroner \n   og protoner hos stabile kjerner")
    print("")
    print("7. Se bar-graf for kokepunkt for hydrokarboner")
    print("")
    print("8. Gå ut")
    print("*"*25)
    tall = int(input("Hva vil du gjøre? (1-8): "))
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

# kokepunkt for hydrokarboner

def plot_noytron_proton_graf():
    plt.plot(x_rett, y_rett, color = "steelblue", label = "Z = N")
    plt.scatter(x_protontall, y_noytrontall, color = "r", s = 10)
    plt.xlabel("Antall protoner $Z$")
    plt.ylabel("Antall nøytroner $N$")
    plt.title("Forholdet mellom protontall og nøytrontall hos stabile kjerner")
    plt.legend(loc = "upper left")
    plt.show()
# plot_noytron_proton_graf()


""" MOLARMASSEKALKULATOR """
# input example "Na2SO4"
def molar_masse_kalkulator(molekyl):
    stoff = fra_navn_til_dict(molekyl)
    molar_masse_resultat = 0
    for key,value in stoff.items():
        objekt_i_periodicTable = finn_grunnstoff(key)
        atom_masse = objekt_i_periodicTable.molarMasse
        print("Stoff:", key, "Atommasse:", atom_masse, "Antall:", value)
        molar_masse_resultat += atom_masse * float(value)

    return molar_masse_resultat

""" BEREGNING AV BINDINGER """
def finn_binding(stoff1, stoff2):
    # metallbinding
    if stoff1.type == "Metal" and stoff2.type == "Metal":
        if stoff1.type == stoff2.type:
            print(f"{stoff1.navn} er metall, og flere danner metallbinding.")
        else:
            print(f"{stoff1.navn} og {stoff2.navn} er begge metaller og danner metallbinding.")

    # kovalent binding
    elif stoff1.type == "Nonmetal" and stoff2.type == "Nonmetal":
        if stoff1.type == stoff2.type:
            print(f"{stoff1.navn} er ikke-metall, og to stykker danner kovalent binding.")
        else:
            print(f"{stoff1.navn} og {stoff2.navn} er begge ikke-metaller og danner kovalent binding.")

    elif stoff1.type == "Metalloid" or stoff2.type == "Metalloid":
        print("Et av stoffene er et halv-metall, binding er ukjent.")
    #ionebinding
    else:
        if stoff1.type == "Nonmetal" and stoff2.type == "Metal":
            print(f"{stoff1.navn} er ikke-metall og {stoff2.navn} er metall og de danner ionebinding.")
        else:
            print(f"{stoff1.navn} er metall og {stoff2.navn} er ikke-metall og de danner ionebinding.")


""" SVAR PÅ BRUKER INPUT """
# kanskje vi bør flytte denne funksjonen til kjemi_utils? 
def finn_grunnstoff(symbol):
    return periodicTable.get(symbol)

def finn_oppgave(tall):
    if tall == 1:        
        bruker_symbol = input("Hvilket grunnstoff har du? Skriv symbol: ").capitalize()
        grunnstoff = finn_grunnstoff(bruker_symbol)
        if grunnstoff:
            m_verdi = int(input("Hvor mange gram har du?: "))
            print(grunnstoff.mol_fra_masse(m_verdi))
        else:
            print("Grunnstoffet ble ikke funnet.")

    elif tall == 2:
        bruker_symbol = input("Hvilket grunnstoff har du? Skriv symbol: ").capitalize()
        grunnstoff = finn_grunnstoff(bruker_symbol)
        if grunnstoff:
            mol = int(input("Hvor mange mol har du?: "))
            print(grunnstoff.mol_til_partikler(mol))
        else:
            print("Grunnstoffet ble ikke funnet.")

    elif tall == 3:
        molekyl_fra_bruker = input("Hvilket stoff vil du finne molarmassen til? Skriv med symboler: ")
        print("Molarmasseresultat: ", molar_masse_kalkulator(molekyl_fra_bruker))
            
    elif tall == 4:
        bruker_symbol1 = input("Hva er det første stoffet? Skriv symbol: ").capitalize()
        bruker_symbol2 = input("Hva er det andre stoffet? Skriv symbol: ").capitalize()
        grunnstoff1 = finn_grunnstoff(bruker_symbol1)
        grunnstoff2 = finn_grunnstoff(bruker_symbol2)
        if grunnstoff1 and grunnstoff2:
            finn_binding(grunnstoff1, grunnstoff2)
        else:
            print("Grunnstoffet ble ikke funnet.")


    elif tall == 5:
        bruker_symbol = input("Hvilket grunnstoff har du? Skriv symbol: ").capitalize()
        grunnstoff = finn_grunnstoff(bruker_symbol)
        if grunnstoff: 
            print(grunnstoff.forhold_mellomm_en_ar())
        else: 
            print("Grunnstoffet ble ikke funnet.")

    elif tall == 6:
        noytroner_protoner()
        rett_linje()
        plot_noytron_proton_graf()
        print("Denne grafen illustrerer et mønster for kjernefysisk stabilitet. I lette atomkjerner er forholdet mellom antall protoner og nøytroner omtrent 1:1, noe som betyr at det er like mange protoner som nøytroner. Etter hvert som atomnummeret øker, blir forholdet skjevere, og de stabile kjernene har flere nøytroner enn protoner. Dette skyldes at de ekstra nøytronene bidrar til å balansere den økende frastøtningen mellom protonene.")

    elif tall == 7:
        pass

tall = 0
while tall != 8:
    tall = print_meny()
    if tall != 8:
        finn_oppgave(tall)
        print("")
        time.sleep(3)
    else:
        print("Avslutter programmet...")
        print("")
        break 

