import functions as func

print("Bitte geben Sie sämtliche Werte ohne Sonderzeichen ein.")

# Eingabewerte
bruttolistenpreis = float(input("Bitte geben Sie den Bruttolistenpreis des Lieferanten ein: "))
ust_satz = float(input("Bitte geben Sie den USt-Satz ein: "))
lieferer_rabatt = float(input("Bitte geben Sie den Lieferer-Rabatt ein: "))
lieferer_skonto = float(input("Bitte geben Sie den Lieferer-Skonto ein: "))
bezugskosten = float(input("Bitte geben Sie die Bezugskosten ein: "))


# Aufruf der Funktion bezugskalkulation
netto_listenpreis, zieleinkaufspreis, bareinkaufspreis, einstandspreis = func.bezugskalkulation(bruttolistenpreis, ust_satz, lieferer_rabatt, lieferer_skonto, bezugskosten)

# Ausgabe der Ergebnisse mit Rundung auf zwei Nachkommastellen
print("Netto-Listenpreis: {: .2f} €".format(netto_listenpreis))
print("Zieleinkaufspreis: {: .2f} €".format(zieleinkaufspreis))
print("Bareinkaufspreis: {: .2f} €".format(bareinkaufspreis))
print("Einstandspreis: {: .2f} €".format(einstandspreis))