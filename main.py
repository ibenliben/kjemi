import time
from kjemi_utils import plot_noytron_proton_graf, plot_hydrokarboner, finn_grunnstoff, molar_masse_kalkulator, finn_binding

# meny
def print_meny():
    """
    Viser en meny funksjoner og returnerer brukerens valg.
    Brukeren blir bedt om å velge et alternativ ved å skrive inn et 
    tall mellom 1 og 8.
    """
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


""" SVAR PÅ BRUKER INPUT """
def finn_oppgave(tall):
    """
    Utfører en oppgave basert på brukerens valg. 
    Parametre: 
        tall (int): Tall mellom 1-8 som representerer brukerens valg fra menyen
    """
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
        plot_noytron_proton_graf()
        print("Denne grafen illustrerer et mønster for kjernefysisk stabilitet. I lette atomkjerner er forholdet mellom antall protoner og nøytroner omtrent 1:1, noe som betyr at det er like mange protoner som nøytroner. Etter hvert som atomnummeret øker, blir forholdet skjevere, og de stabile kjernene har flere nøytroner enn protoner. Dette skyldes at de ekstra nøytronene bidrar til å balansere den økende frastøtningen mellom protonene.")

    elif tall == 7:
        plot_hydrokarboner()
        print("Dette er en graf som illustrerer kokepunktet til alkaner. Vi ser at dette illustrerer en tydelig trend der for antall karbonatomer i et alkan, jo høyere kokepunkt. Dette er fordi de totale kreftene mellom alkan-molekylene øker når molekylet blir større, altså når det blir satt inn flere C-atomer.")

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

