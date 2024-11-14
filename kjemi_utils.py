def fra_navn_til_dict(molekyl):
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