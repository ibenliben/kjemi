import csv
from grunnstoff import Grunnstoff
import matplotlib.pyplot as plt
import numpy as np


filnavn = "PeriodicTable.csv"                         # csv-filen
periodicTable = {}                                    # dictionary = {symbol; grunnstoffobjekt}

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    
    # hoppe over overskrifter
    overskrifter = next(filinnhold)

    for rad in filinnhold:
        # lage objekt, gi navn 
        g = Grunnstoff(*rad)                                #explode list to parameters
        periodicTable[g.symbol] = g


def finn_grunnstoff(symbol):
    return periodicTable.get(symbol)


""" GRAFPLOT """
# forhold mellom nøytroner og atomnummer, graf
def plot_noytron_proton_graf():
    x_protontall = []
    y_noytrontall = []
    for key, grunnstoff in periodicTable.items():
        x_protontall.append(grunnstoff.atomnummer)
        y_noytrontall.append(grunnstoff.noytron)

# lage rett linje for sammenlikning
    x_rett = []
    y_rett = []
    for i in range(170):
        x_rett.append(i)
        y_rett.append(i)

    plt.plot(x_rett, y_rett, color = "steelblue", label = "Z = N")
    plt.scatter(x_protontall, y_noytrontall, color = "r", s = 10)
    plt.xlabel("Antall protoner $Z$")
    plt.ylabel("Antall nøytroner $N$")
    plt.title("Forholdet mellom protontall og nøytrontall hos stabile kjerner")
    plt.legend(loc = "upper left")
    plt.show()

# kokepunkt for hydrokarboner graf
def plot_hydrokarboner():
    C_atomer = [1, 2, 3, 4, 5, 6, 7]
    kokepunkt = np.array([-162, -89, -42, 0, 36, 69, 98])
    offset = -180

    plt.bar(C_atomer, kokepunkt-offset, color = "lightblue", bottom = offset)
    plt.xlabel("Antall C-atomer i alkaner")
    plt.ylabel("Kokepunkt (°C)")
    plt.axhline(y = 20, color = "red")
    plt.text(0.5, 22, "Romtemperatur (20°C)", color = "red", ha = "left", va = "bottom")

    y_max = max(kokepunkt) + 40
    plt.ylim(offset, y_max)

    for x, y in zip(C_atomer, kokepunkt):
        plt.text(x, y + 5, f"{y}°C", ha = "center", va = "bottom")

    plt.show()


""" MOLARMASSEKALKULATOR """
def fra_navn_til_dict(molekyl):
    """
    Konverterer en kjemisk formel til en ordbok som representerer grunnstoffene og antallet av dem.

    Parametre:
        molekyl (str): Den kjemiske formelen for et molekyl.

    Returns:
        dict: En ordbok med grunnstoff som nøkler og antall som verdier.
        str: Returnerer "ugyldig stoff." hvis formelen inneholder ugyldige tegn.

    Eksempel:
        >>> fra_navn_til_dict("Na2SO4")
        {'Na': 2, 'S': 1, 'O': 4}
    """
    dict = {}
    stoff = ""
    for indeks, bokstav in enumerate(molekyl):                  # enumerate gir tilgang til både indeks og bokstav
        if bokstav.isalpha():
            if bokstav.isupper():
                if stoff:
                    dict[stoff] = antall
                stoff = bokstav
                antall = 1
            else: 
                stoff += bokstav
        elif bokstav.isdigit():
            if indeks > 0 and molekyl[indeks-1].isdigit():      # håndterer tall med flere siffer
                antall = antall * 10 + int(bokstav)  
            else:
                antall = int(bokstav)
        else:
            return "ugyldig stoff."
    if stoff:
        dict[stoff] = antall

    return dict

def molar_masse_kalkulator(molekyl):
    """
    Beregner molarmassen til et molekyl basert på den kjemiske formelen.

    Parametre:
        molekyl (str): Den kjemiske formelen for et molekyl.

    Returns:
        Den totale molarmassen til molekylet i g/mol. (float)

    Eksempel:
        >>> molar_masse_kalkulator("Na2SO4")
        Stoff: Na Atommasse: 22.99 Antall: 2
        Stoff: S Atommasse: 32.06 Antall: 1
        Stoff: O Atommasse: 16.0 Antall: 4
        142.04
    """
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
    """
    Beregner bindingen mellom to stoffer basert på typen.

    Parametre:
        stoff1 (str): Det kjemiske symbolet for et grunnstoff
        stoff2 (str): Det kjemiske symbolet for det andre grunnstoffet

    Eksempel:
        >>> finn_binding("Na", "Cl")
        Natrium er ikke-metall og Chlorine er metall og de danner ionebinding.
    """
    # metallbinding
    if stoff1.type == "Metal" and stoff2.type == "Metal":
        if stoff1.navn == stoff2.navn:
            print(f"{stoff1.navn} er metall, og flere danner metallbinding.")
        else:
            print(f"{stoff1.navn} og {stoff2.navn} er begge metaller og danner metallbinding.")

    # kovalent binding
    elif stoff1.type == "Nonmetal" and stoff2.type == "Nonmetal":
        if stoff1.navn == stoff2.navn:
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