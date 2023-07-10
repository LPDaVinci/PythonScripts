
import functions as func

# Auswahl zwischen Bezugskalkulation und Handelskalkulation
auswahl = input("Bitte wählen Sie zwischen 'Bezugskalkulation' und 'Handelskalkulation': ")

if auswahl.lower() == "bezugskalkulation":
    # Eingabe für Bezugskalkulation
    bruttolistenpreis = func.parse_value(input("Bruttolistenpreis des Lieferanten: "))
    ust_satz = func.parse_value(input("USt-Satz in Prozent: "))
    lieferer_rabatt = func.parse_value(input("Lieferer-Rabatt in Prozent: "))
    lieferer_skonto = func.parse_value(input("Lieferer-Skonto in Prozent: "))
    bezugskosten = func.parse_value(input("Bezugskosten: "))

    netto_listenpreis, zieleinkaufspreis, bareinkaufspreis, einstandspreis = func.bezugskalkulation(bruttolistenpreis, ust_satz, lieferer_rabatt, lieferer_skonto, bezugskosten)

    # Ausgabe der Ergebnisse
    print("Netto-Listenpreis:", netto_listenpreis)
    print("Zieleinkaufspreis:", zieleinkaufspreis)
    print("Bareinkaufspreis:", bareinkaufspreis)
    print("Einstandspreis:", einstandspreis)

elif auswahl.lower() == "handelskalkulation":
    # Eingabe für Handelskalkulation
    bezugspreis = func.parse_value(input("Bezugspreis: "))
    handlungskostenzuschlag = func.parse_value(input("Handlungskostenzuschlag in Prozent: "))
    gewinnzuschlag = func.parse_value(input("Gewinnzuschlag in Prozent: "))
    rabattsatz = func.parse_value(input("Rabattsatz in Prozent: "))
    skontosatz = func.parse_value(input("Skontosatz in Prozent: "))
    ust_satz = func.parse_value(input("USt-Satz in Prozent: "))

    barverkaufspreis, zielverkaufspreis, listenverkaufspreis_netto, listenverkaufspreis_brutto = func.handelskalkulation(bezugspreis, handlungskostenzuschlag, gewinnzuschlag, rabattsatz, skontosatz, ust_satz)

    # Ausgabe der Ergebnisse
    print("Barverkaufspreis:", barverkaufspreis)
    print("Zielverkaufspreis:", zielverkaufspreis)
    print("Listenverkaufspreis netto:", listenverkaufspreis_netto)
    print("Listenverkaufspreis brutto:", listenverkaufspreis_brutto)

else:
    print("Ungültige Auswahl.")
