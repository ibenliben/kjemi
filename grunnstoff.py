class Grunnstoff:
    def __init__(self, navn, atomnummer, symbol, molarMasse, noytron, periode, gruppe, fase, type, elektronegativitet, atomradius):
        self.navn = navn
        self.atomnummer = int(atomnummer)
        self.symbol = symbol
        self.molarMasse = float(molarMasse)
        self.noytron = int(noytron)
        self.periode = int(periode)
        self.gruppe = int(gruppe) if gruppe else 0
        self.fase = fase
        self.type = type
        self.elektronegativitet = float(elektronegativitet) if elektronegativitet else 0
        self.atomradius = float(atomradius) if atomradius else 0

    def __str__(self): 
        return f"Grunnstoffet {self.navn} har atomnummer {self.atomnummer} og symbol {self.symbol}."
    
    def forholdMellomENogAR(self):
        #TO DO
        pass
    