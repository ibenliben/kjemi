import matplotlib.pyplot as plt
import numpy as np 

filnavn = "PeriodicTable.csv"                         # csv-filen
periodicTable = {}                                    # dictionary = {symbol; grunnstoffobjekt}


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
