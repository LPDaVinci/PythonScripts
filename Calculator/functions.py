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

def parse_value(value):
    if value[-1] == "€":
        return float(value[:-1])
    elif value[-1] == "%":
        return float(value[:-1])
    else:
        return float(value)

def round_decimal(value):
    return round(value, 2)

def bezugskalkulation(bruttolistenpreis, ust_satz, lieferer_rabatt, lieferer_skonto, bezugskosten):
    netto_listenpreis = bruttolistenpreis * (1 + ust_satz/100)
    zieleinkaufspreis = netto_listenpreis - (netto_listenpreis * lieferer_rabatt/100)
    bareinkaufspreis = zieleinkaufspreis - (zieleinkaufspreis * lieferer_skonto/100)
    einstandspreis = bareinkaufspreis + bezugskosten
    
    return round_decimal(netto_listenpreis), round_decimal(zieleinkaufspreis), round_decimal(bareinkaufspreis), round_decimal(einstandspreis)

def handelskalkulation(bezugspreis, handlungskostenzuschlag, gewinnzuschlag, rabattsatz, skontosatz, ust_satz):
    barverkaufspreis = bezugspreis + (bezugspreis * handlungskostenzuschlag/100) + (bezugspreis * gewinnzuschlag/100)
    zielverkaufspreis = barverkaufspreis + (barverkaufspreis * rabattsatz/100)
    listenverkaufspreis_netto = zielverkaufspreis / (1 + ust_satz/100)
    listenverkaufspreis_brutto = listenverkaufspreis_netto * (1 + ust_satz/100)
    
    return round_decimal(barverkaufspreis), round_decimal(zielverkaufspreis), round_decimal(listenverkaufspreis_netto), round_decimal(listenverkaufspreis_brutto)


