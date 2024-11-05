class Grunnstoff:
    def __init__(self, navn, atomnummer, symbol, molarMasse, noytron, periode, gruppe, fase, type, elektronegativitet, atomradius):
        self.navn = navn
        self.atomnummer = atomnummer
        self.symbol = symbol
        self.molarMasse = molarMasse
        self.noytron = noytron
        self.periode = periode
        self.gruppe = gruppe
        self.fase = fase
        self.type = type
        self.elektronegativitet = elektronegativitet
        self.atomradius = atomradius

    def __str__(self):    #Hvordan grunnstoffet skal se ut som en string
        return f"Grunnstoffet {self.navn} har atomnummer {self.atomnummer} og symbol {self.symbol}."
    
    