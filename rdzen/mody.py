class Modyfikacje():
    def __init__(self, cena: float, czas: int, przyrost_koni : int, naped: str = None , limit_koni: int = None):
        self.cena = cena
        self.czas = czas
        self.naped = naped
        self.limit_koni = limit_koni
        self.przyrost_koni = przyrost_koni
class Samochod():
    def __init__(self, nazwa: str, r_naped: str, konie: int, kuty: bool, rejestracja: str, zamontowane_mody: list = None):
        self.kuty = kuty
        self.nazwa = nazwa
        self.r_naped = r_naped
        self.konie = konie
        self.rejestracja = rejestracja
        if zamontowane_mody is None:
            self.zamontowane_mody = []
        else:
            self.zamontowane_mody = zamontowane_mody
        self.koszyk = []
class Kierownik:
    def zamontuj(self, auto : Samochod, mod : Modyfikacje):
        if mod.naped is not None:
            if mod.naped != auto.r_naped:
                print("niepasuje naped")
                return False

        if mod.limit_koni is not None:
            if mod.przyrost_koni + auto.konie > mod.limit_koni:
                if not auto.kuty:
                    print("za duzo koni")
                    return False
        auto.koszyk.append(mod)
        return True
    def podlicz(self, auto : Samochod):
        suma_cena = 0
        suma_czas = 0
        for modzik in auto.koszyk:
            suma_cena += modzik.cena
            suma_czas += modzik.czas

        return suma_cena, suma_czas

