class Produkt:
    def __init__(self, nazwa: str, cena: int):
        self.nazwa = nazwa
        self.cena = cena

    def __repr__(self):
        return (f"{self.nazwa} ({self.cena} zł)")

class Zamowienie:
    def __init__(self, numer: int):
        self.numer = numer
        self.produkty = []

    def dodaj_produkt(self, produkt: Produkt, ilosc=1):
        if isinstance(produkt, Produkt):
            self.produkty.extend([produkt]*ilosc)
    def laczna_wartosc(self):
        wartosc = 0
        for produkt in self.produkty:
            wartosc += produkt.cena
        return f"lacznie {wartosc} zł"
    def pokaz_zamowienie(self):
        print(f"zamowienie numer: {self.numer}, produkty: {self.produkty}")
        print(f"{self.laczna_wartosc()}")

p1 = Produkt("Chleb", 5)
p2 = Produkt("Konserwa", 5)
z1 = Zamowienie(1)
z1.dodaj_produkt(p1, 2)
z1.dodaj_produkt(p2, 3)
z1.pokaz_zamowienie()
