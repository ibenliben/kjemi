from kjemi_utils import fra_navn_til_dict

stoff = "Na2SO4"
expected = {"Na":2, "S":1, "O":4}
resultat = fra_navn_til_dict(stoff)

if resultat != expected:
    print("Feil resultat for", stoff, "forventet", expected, "Men fikk", resultat)