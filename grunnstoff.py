class Grunnstoff:
    """
    Klasse for å lage grunnstoff-objekter.
    Parametre:
        navn (str): Grunnstoffets navn
        atomnummer (int): Grunnstoffets nummer i periodesystemet
        symbol (str): Grunnstoffets forkortelse. f.eks "Na" for "Natrium"
        molar_masse (float): Atommassen til grunnstoffet
        noytron (int): Antall nøytroner i det vanligste isotopet av grunnstoffet
        periode (int): Raden i periodesystemet vi finner grunnstoffet
        gruppe = 0 (int): Kolonnen til grunnstoffet i periodesystemet
        fase (str): Grunnstoffets fase (g, l, s) i romtemperatur
        type (str): Metall, halv-metall eller ikke-metall
        elektronegativitet = 0 (float): Grunnstoffets evne til å trekke til seg elektroner 
        atomradius = 0 (float): Atomradiusen til grunnstoffet
    """
    def __init__(self, navn, atomnummer, symbol, molar_masse, noytron, periode, gruppe, fase, type, elektronegativitet, atomradius):
        """
        Konstruktør
        """
        self.navn = navn
        self.atomnummer = int(atomnummer)
        self.symbol = symbol
        self.molar_masse = float(molar_masse)
        self.noytron = int(noytron)
        self.periode = int(periode)
        self.gruppe = int(gruppe) if gruppe else 0
        self.fase = fase
        self.type = type
        self.elektronegativitet = float(elektronegativitet) if elektronegativitet else 0
        self.atomradius = float(atomradius) if atomradius else 0

    def __str__(self): 
        """
        Returnerer en lesbar strengrepresentasjon av grunnstoffet.
        """
        return f"Grunnstoffet {self.navn} har atomnummer {self.atomnummer} og symbol {self.symbol}."
    
    def forhold_mellom_en_ar(self):
        """
        Returnerer forholdet mellom elektronegativiteten og atomradiusen til grunnstoffet.
        """
        if self.elektronegativitet and self.atomradius:
            return f"Forholdet mellom elektronegativitet og atomradius til {self.navn} er: {(self.elektronegativitet / self.atomradius):.3f}"
        
        else:
            return f"Vi har ikke informasjon om {self.navn} sin elektronegativitet og/eller atomradius"

# omregning fra masse(m) til mol(n) 
    def mol_fra_masse(self, m):
        """
        Returnerer stoffmengden av grunnstoffet ved input masse.
        Parametre: 
            m (float): Massen(i gram) du vil omregne til stoffmengde.
        """
        n = m / self.molar_masse
        return f"{m} gram av {self.navn} tilsvarer {n:.3f} mol"
    
    def mol_til_partikler(self, n):
        """
        Returnerer antall partikler av grunnstoffet ved input stoffmengde
        Parametre: 
            n (float): Stoffmengden(i mol) du vil omregne til antall partikler. 
        """
        avo = 6.022140 * 10**23
        partikler = n * avo

        # formaterer med 10^ notasjon
        base, eksponent = f"{partikler:.6e}".split("e")
        eksponent = int(eksponent)

        return f"{n} mol av {self.navn} tilsvarer {base}*10^{eksponent} partikler"