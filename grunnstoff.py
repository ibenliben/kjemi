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
    
    def forhold_mellomm_en_ar(self):
        #TO DO
        pass

# omregning fra masse(m) til mol(n) 
# må fikses så man kan ta input fra bruker
    def mol_fra_masse(self, m):
        n = m / self.molarMasse
        return f"{m} gram av {self.navn} tilsvarer {n} mol"
    
    def mol_til_partikler(self, n):
        avo = 6.022140 * 10**23
        partikler = n * avo

        # formaterer med 10^ notasjon
        base, eksponent = f"{partikler:.6e}".split("e")
        eksponent = int(eksponent)

        return f"{n} mol av {self.navn} tilsvarer {base}*10^{eksponent} partikler"
    