import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class CalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kalkulator")
        
        self.create_widgets()
        
        self.window.mainloop()
    
    def create_widgets(self):
        self.label = tk.Label(self.window, text="Bitte wählen Sie eine Option:")
        self.label.pack()
        
        self.option = tk.StringVar()
        self.option.set("Bezugskalkulation")
        self.radio_be = tk.Radiobutton(self.window, text="Bezugskalkulation", variable=self.option, value="Bezugskalkulation")
        self.radio_be.pack()
        self.radio_hk = tk.Radiobutton(self.window, text="Handelskalkulation", variable=self.option, value="Handelskalkulation")
        self.radio_hk.pack()
        
        self.btn_calc = tk.Button(self.window, text="Berechnen", command=self.calculate)
        self.btn_calc.pack()
        
    def calculate(self):
        choice = self.option.get()
        
        if choice == "Bezugskalkulation":
            bruttolistenpreis = float(tk.simpledialog.askstring("Bezugskalkulation", "Bruttolistenpreis des Lieferanten:"))
            ust_satz = float(tk.simpledialog.askstring("Bezugskalkulation", "USt-Satz in Prozent:"))
            lieferer_rabatt = float(tk.simpledialog.askstring("Bezugskalkulation", "Lieferer-Rabatt in Prozent:"))
            lieferer_skonto = float(tk.simpledialog.askstring("Bezugskalkulation", "Lieferer-Skonto in Prozent:"))
            bezugskosten = float(tk.simpledialog.askstring("Bezugskalkulation", "Bezugskosten:"))
            
            netto_listenpreis, zieleinkaufspreis, bareinkaufspreis, einstandspreis = self.bezugskalkulation(bruttolistenpreis, ust_satz, lieferer_rabatt, lieferer_skonto, bezugskosten)
            
            messagebox.showinfo("Ergebnisse", f"Barverkaufspreis: {barverkaufspreis}\nZielverkaufspreis: {zielverkaufspreis}\nListenverkaufspreis netto: {listenverkaufspreis_netto}\nListenverkaufspreis brutto: {listenverkaufspreis_brutto}")

        elif choice == "Handelskalkulation":
            bezugspreis = float(tk.simpledialog.askstring("Handelskalkulation", "Bezugspreis:"))
            handlungskostenzuschlag = float(tk.simpledialog.askstring("Handelskalkulation", "Handlungskostenzuschlag in Prozent:"))
            gewinnzuschlag = float(tk.simpledialog.askstring("Handelskalkulation", "Gewinnzuschlag in Prozent:"))
            rabattsatz = float(tk.simpledialog.askstring("Handelskalkulation", "Rabattsatz in Prozent:"))
            skontosatz = float(tk.simpledialog.askstring("Handelskalkulation", "Skontosatz in Prozent:"))
            ust_satz = float(tk.simpledialog.askstring("Handelskalkulation", "USt-Satz in Prozent:"))
            
            barverkaufspreis, zielverkaufspreis, listenverkaufspreis_netto, listenverkaufspreis_brutto = self.handelskalkulation(bezugspreis, handlungskostenzuschlag, gewinnzuschlag, rabattsatz, skontosatz, ust_satz)
            
            messagebox.showinfo("Ergebnisse", f"Barverkaufspreis: {barverkaufspreis}\nZielverkaufspreis: {zielverkaufspreis}\nListenverkaufspreis netto: {listenverkaufspreis_netto}\nListenverkaufspreis brutto: {listenverkaufspreis_brutto}")

        else:
            messagebox.showerror("Fehler", "Ungültige Auswahl.")
    
    def bezugskalkulation(self, bruttolistenpreis, ust_satz, lieferer_rabatt, lieferer_skonto, bezugskosten):
        netto_listenpreis = bruttolistenpreis * (1 + ust_satz/100)
        zieleinkaufspreis = netto_listenpreis - (netto_listenpreis * lieferer_rabatt/100)
        bareinkaufspreis = zieleinkaufspreis - (zieleinkaufspreis * lieferer_skonto/100)
        einstandspreis = bareinkaufspreis + bezugskosten
        
        return round(netto_listenpreis, 2), round(zieleinkaufspreis, 2), round(bareinkaufspreis, 2), round(einstandspreis, 2)
    
    def handelskalkulation(self, bezugspreis, handlungskostenzuschlag, gewinnzuschlag, rabattsatz, skontosatz, ust_satz):
        barverkaufspreis = bezugspreis + (bezugspreis * handlungskostenzuschlag/100) + (bezugspreis * gewinnzuschlag/100)
        zielverkaufspreis = barverkaufspreis + (barverkaufspreis * rabattsatz/100)
        listenverkaufspreis_netto = zielverkaufspreis / (1 + ust_satz/100)
        listenverkaufspreis_brutto = listenverkaufspreis_netto * (1 + ust_satz/100)
        
        return round(barverkaufspreis, 2), round(zielverkaufspreis, 2), round(listenverkaufspreis_netto, 2), round(listenverkaufspreis_brutto, 2)

# Starte die GUI
gui = CalculatorGUI()
