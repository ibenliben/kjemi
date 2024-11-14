def fra_navn_til_dict(molekyl):
    dict = {}
    
    for bokstav in molekyl:
        stoff = ""
        if bokstav.isalpha():
            if bokstav.isupper():
                if stoff:
                    dict[stoff] = antall
                stoff = bokstav
                antall = 1
            else: 
                stoff += bokstav

        elif bokstav.isdigit():
            antall = bokstav
        
        else:
            return "ugyldig stoff."
    
    dict[stoff] = antall