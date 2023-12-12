import functions as func

print("Bitte geben Sie sämtliche Werte ohne Sonderzeichen ein.")

# Auswahl der Kalkulationsart
kalkulationsart = input("Bitte wählen Sie die Kalkulationsart (Bezugskalkulation/Handelskalkulation): ")

if kalkulationsart.lower() == "bezugskalkulation":
    # Eingabewerte für die Bezugskalkulation
    bruttolistenpreis = float(input("Bitte geben Sie den Bruttolistenpreis des Lieferanten ein: "))
    ust_satz = float(input("Bitte geben Sie den USt-Satz ein: "))
    lieferer_rabatt = float(input("Bitte geben Sie den Lieferer-Rabatt ein: "))
    lieferer_skonto = float(input("Bitte geben Sie den Lieferer-Skonto ein: "))
    bezugskosten = float(input("Bitte geben Sie die Bezugskosten ein: "))

    # Aufruf der Funktion bezugskalkulation
    netto_listenpreis, zieleinkaufspreis, bareinkaufspreis, einstandspreis = func.bezugskalkulation(bruttolistenpreis, ust_satz, lieferer_rabatt, lieferer_skonto, bezugskosten)

    # Ausgabe der Ergebnisse in Euro und Prozent
    print("Netto-Listenpreis: {:.2f} Euro".format(netto_listenpreis))
    print("Zieleinkaufspreis: {:.2f} Euro".format(zieleinkaufspreis))
    print("Bareinkaufspreis: {:.2f} Euro".format(bareinkaufspreis))
    print("Einstandspreis: {:.2f} Euro".format(einstandspreis))

elif kalkulationsart.lower() == "handelskalkulation":
    # Eingabewerte für die Handelskalkulation
    einstandspreis = float(input("Bitte geben Sie den Einstandspreis ein: "))
    gewinnspanne = float(input("Bitte geben Sie die Gewinnspanne ein: "))

    # Aufruf der Funktion handelskalkulation
    verkaufspreis = func.handelskalkulation(einstandspreis, gewinnspanne)

    # Ausgabe des Verkaufspreises
    print("Verkaufspreis: {:.2f} Euro".format(verkaufspreis))

else:
    print("Ungültige Auswahl der Kalkulationsart.")