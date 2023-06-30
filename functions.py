# first.py
def foo(): 
    print("foo")

# bezugskalkulation
def bezugskalkulation(bruttolistenpreis, ust_satz, lieferer_rabatt, lieferer_skonto, bezugskosten):
    # Berechnung des Netto-Listenpreises
    netto_listenpreis = bruttolistenpreis / (1 + ust_satz / 100)

    # Berechnung des Zieleinkaufspreises
    zieleinkaufspreis = netto_listenpreis * (1 - lieferer_rabatt / 100)

    # Berechnung des Bareinkaufspreises
    bareinkaufspreis = zieleinkaufspreis - zieleinkaufspreis * (lieferer_skonto / 100)

    # Berechnung des Einstandspreises
    einstandspreis = bareinkaufspreis + bezugskosten

    # Rückgabe der Ergebnisse
    return netto_listenpreis, zieleinkaufspreis, bareinkaufspreis, einstandspreis

# handelskalkulation
def handelskalkulation(einstandspreis, gewinnspanne):
    # Berechnung des Verkaufspreises
    verkaufspreis = einstandspreis * (1 + gewinnspanne / 100)

    # Rückgabe des Verkaufspreises
    return verkaufspreis

